import allure
import pytest
from dotenv import load_dotenv

from tools.cluster.ssh import SSHConnect
from tools.logger.logger import get_logger


load_dotenv()
logger = get_logger('cluster_parsing')


class ClusterLog:
    """Класс парсинга лога кластера на наличие внутренних сбоев и ошибок"""

    @staticmethod
    def mark_start_test_in_cluster_log(
        instance_ssh: SSHConnect,
        message: str,
        node: str
    ):
        """
        Метод для маркировки начало парсинга
        кластер лога с момента теста.
        """
        data = instance_ssh.execute_command(
            command=f'logger -p local0.info -H {node} -t info "{message}"',
            dump=False,
            checking=False)

        return data

    @staticmethod
    def find_in_cluster_log(
        instance_ssh: SSHConnect,
        info: str,
        pathtofile: str = '/var/log/cluster.log',
        line_count: int = 2000,
    ):
        """
        Метод для поиска информации в логе кластера на определенной ноде.
        Параметры:
            :info: str информация, которую нужно найти в логе
            :node_name: str имя ноды, на которой нужно найти информацию
            :pathtofile: str путь к файлу, в котором нужно найти информацию
            :line_count: int количество строк
        """
        data = instance_ssh.execute_command(
            command=f'grep -rin -A {line_count} "{info}" {pathtofile}',
            dump=False,
            checking=False)
        data = data.splitlines()

        return data

    @staticmethod
    def check_for_core_dumps(dump_data):
        """
        Метод проверки наличия 'core dumps' или 'already exists' во входящих данных.
        Если есть то вызываем падение теста и прикрепляем данные к аллюру.
        """
        core_dumps = [line for line in dump_data
                      if 'core dumped' in line
                      or 'already exists' in line]

        if len(core_dumps) > 0:
            message = (
                "\n\nCritical entries found in file <</var/log/messages>>:"
                "\n{}".format("\n".join(core_dumps)))
            logger.critical(message)
            allure.attach(
                message,
                name='messages',
                attachment_type=allure.attachment_type.TEXT,
                extension="attach")
            pytest.fail(reason='Критические записи найдены в файле <</var/log/messages>>')

        else:
            message = (
                "\nNo critical entries were found in the cluster log. All records log:"
                "\n{}".format("\n".join(core_dumps)))
            allure.attach(
                message,
                name='messages',
                attachment_type=allure.attachment_type.TEXT,
                extension="attach")
            logger.info(message)

    @staticmethod
    def check_errors_in_cluster_log(cluster_log: list):
        """
        Метод проверки в логе кластера ошибки, помеченные '###'.
        Если есть то вызывает падение теста и прикрепляем
        строки с ошибками к аллюру.
        """
        error_lines = [line for line in cluster_log
                       if ('###' in line and '####' not in line
                           and '#####' not in line)]

        if len(error_lines) > 0:
            logger.critical(f"Found errors marked '###' in cluster:\n{error_lines}")
            allure.attach(
                '\n'.join(line for line in error_lines),
                name='errors in cluster.log',
                attachment_type=allure.attachment_type.TEXT,
                extension="attach")
            pytest.fail(reason="Найдены промаркированные ошибки '###' в кластере")

        else:
            allure.attach(
                "Промаркированные ошибки '###' не обнаружены",
                name='errors in cluster.log',
                attachment_type=allure.attachment_type.TEXT,
                extension="attach")
            logger.info("Errors marked '###' not found")

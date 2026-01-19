import os
import allure
import pytest
import pytz
from datetime import datetime
from dotenv import load_dotenv

from tools.logger.logger import get_logger
from tools.cluster.parsing import ClusterLog
from tools.cluster.ssh import SSHConnect as SSH


load_dotenv()
logger = get_logger("CLUSTER_LOG")


@pytest.fixture(scope='function', autouse=True)
def parse_cluster_logs(request):
    """
    Фикстура парсинга лога кластера в зависимости от успользуемого в тесте url.
    Перед началом каждого теста делает запись в логе
    кластера в формате "start test {имя теста}{timestamp}"
    После завершения теста проверяем лог кластера
    с момента запуска теста на наличие ошибок.
    """
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S") + ':' + str(now.microsecond // 1000).zfill(2)
    day = now.day
    month = now.strftime("%B")
    year = now.year
    test_name = request.node.name
    message = f"start test {test_name} {formatted_time} {day} {month} {year}"
    
    node_name = "q7u005.z.vstack.com"
    node = 'q7u005'

    pars_log = SSH(
        user_name='root',
        ip_host=node_name,
        private_key=os.getenv('PRIVATE_KEY_CLUSTER_LOG'),
        private_key_pass=os.getenv('PRIVATE_KEY_pass'))
    pars_log.private_key_connect(dump=False)

    ClusterLog.mark_start_test_in_cluster_log(
        instance_ssh=pars_log,
        message=message,
        node=node)
    tz_NY = pytz.timezone('Europe/London')
    now = datetime.now(tz_NY)
    current_time = now.strftime("%H:%M:%S")

    yield

    data = ClusterLog.find_in_cluster_log(
        instance_ssh=pars_log,
        info=message)
    data_to_print = "\n".join(line for line in data)
    allure.attach(
        data_to_print,
        name='cluster.log',
        attachment_type=allure.attachment_type.TEXT,
        extension="attach")

    dump_data = ClusterLog.find_in_cluster_log(
        instance_ssh=pars_log,
        info=current_time,
        pathtofile='/var/log/messages')
    ClusterLog.check_for_core_dumps(dump_data)
    ClusterLog.check_errors_in_cluster_log(cluster_log=data)

    pars_log.close_channel()

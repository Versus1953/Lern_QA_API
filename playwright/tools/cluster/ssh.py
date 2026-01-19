import time
import pytest
from io import StringIO
import logging
from typing import Literal, Union, Optional
import socket


from dotenv import load_dotenv
import paramiko

from tools.logger.logger import get_logger

load_dotenv()
logger = get_logger('SSH')


class SSHConnect:
    """Класс для методов и настроек ssh-соединения"""

    def __init__(
        self,
        user_name: str,
        ip_host: str,
        port: int = 22,
        private_key: Optional[str] = None,
        private_key_pass: Optional[str] = None,
        user_password: Optional[str] = None,
        RunTimeout: int = 90
    ):
        """
        Инициализатор класса SSH-соединения
        Ожидает аргументы:
            1. ip_host - адрес или DNS хоста (обязательный);
            2. user_name - имя пользователя в запрашиваемом хосте;
            2. user_password - пароль пользователя в запрашиваемом хосте
               для метода password_connect;
            3. port - порт хоста (по дефолту 22)
            4. private_key - приватный ключ для метода private_key_connect;
            5. private_key_pass - доп пароль для приватного ключа;
            6. RunTimeout - время попытки соединения по SSH
        """
        self.ip_host = ip_host
        self.user_name = user_name
        self.user_password = user_password
        self.port = port
        self.private_key = private_key
        self.private_key_pass = private_key_pass
        self.RunTimeout = RunTimeout
        self.session: paramiko.SSHClient = None
        self.async_session = None

    def password_connect(self, dump: bool = True) -> paramiko.SSHClient:
        """Авториция пользователя ssh-соединения по логину и паролю."""
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection = False
        start_time = time.time()
        attempts_time = 0

        if dump:
            print(f'Попытка подключения к ip {self.ip_host} порт {self.port}')
            logger.info(f'Trying to connect to ip {self.ip_host} port {self.port}')

        while not connection:
            try:
                attempts_time = time.time() - start_time

                if attempts_time > self.RunTimeout:
                    message = 'SSH timeout exceeded on host'
                    logger.critical(f'{message}: ip {self.ip_host} port {self.port}')
                    pytest.fail(reason=message)

                session.connect(
                    hostname=self.ip_host,
                    port=self.port,
                    username=self.user_name,
                    password=self.user_password)
                connection = True

                if dump:
                    print(f'SSH соединение ip {self.ip_host} установлено')
                    logger.info(f'SSH connection ip {self.ip_host} established')

            except Exception as error:
                msg = "Non-critical connection attempt error"
                time.sleep(1)
                print(f'{msg}, {error}')
                logger.error(f'{msg}, {error}')

        self.session = session

    def private_key_connect(
        self,
        type_pkey: Literal['RSA', 'Ed25519', 'ECDSA'] = 'Ed25519',
        dump: bool = True
    ) -> paramiko.SSHClient:
        """Авторизация пользователя ssh-соединения по приватному ключу."""
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection = False
        start_time = time.time()
        attempts_time = 0
        private_key_str = self.private_key.replace('\\n', '\n')
        input_pkey = StringIO(private_key_str)

        if dump:
            print(f'Попытка подключения к ip {self.ip_host} порт {self.port}')
            logger.info(f'Trying to connect to ip {self.ip_host} port {self.port}')

        if type_pkey == 'RSA':
            private_key = paramiko.RSAKey.from_private_key(
                input_pkey,
                password=self.private_key_pass)
        elif type_pkey == 'Ed25519':
            private_key = paramiko.Ed25519Key.from_private_key(
                input_pkey,
                password=self.private_key_pass)
        else:
            private_key = paramiko.ECDSAKey.from_private_key(
                input_pkey,
                password=self.private_key_pass)

        while not connection:
            try:
                attempts_time = time.time() - start_time

                if attempts_time > self.RunTimeout:
                    message = 'SSH timeout exceeded on host'
                    logger.critical(f'{message}: ip {self.ip_host} port {self.port}')
                    pytest.fail(reason=message)

                session.connect(
                    hostname=self.ip_host,
                    port=self.port,
                    username=self.user_name,
                    pkey=private_key)
                connection = True

                if dump:
                    print(f'SSH соединение ip {self.ip_host} установлено')
                    logger.info(f'SSH connection ip {self.ip_host} established')

            except Exception as error:
                msg = "Non-critical connection attempt error"
                time.sleep(1)
                print(f'{msg}, {error}')
                logging.error(f'{msg}, {error}')

        self.session = session

    def execute_command(
        self,
        command: str,
        run_timeout: Union[int, None] = None,
        use_pty: bool = False,
        show_result: Literal['interim', 'final'] = 'final',
        dump: bool = True,
        checking: bool = True,
    ):
        """
        Метод исполнения консольной команды ssh-соединения.
        Работает в 2-х режимах вывода резульатов:
            1. Конечный ответ на команду (в режиме final);
            2. Построчный вывод результата (в режиме interim)
        """
        try:
            if self.session is None:
                msg_act_chan = 'No active channel with host'
                logger.critical(f'{msg_act_chan} ip {self.ip_host}')
                pytest.fail(reason=msg_act_chan)

            if dump:
                print(f"Хост {self.ip_host} команда: <<{command}>>")
                logger.info(f"Host {self.ip_host} command: <<{command}>>")

            _, stdout, stderr = self.session.exec_command(
                command=command,
                timeout=run_timeout,
                get_pty=use_pty)

            if show_result == 'final':
                exit_status = stdout.channel.recv_exit_status()
                output = stdout.read().decode('utf-8', errors='ignore')
                error_output = stderr.read().decode('utf-8', errors='ignore')

            elif show_result == 'interim':
                output_list = []
                error_output_list = []

                while not stdout.channel.exit_status_ready():
                    if stdout.channel.recv_ready():
                        line = stdout.readline().decode('utf-8', errors='ignore').strip()
                        if line:
                            output_list.append(line)
                            print(line)

                    if stderr.channel.recv_ready():
                        error_line = stderr.readline().decode('utf-8', errors='ignore').strip()
                        if error_line:
                            error_output_list.append(error_line)
                            print(error_line)

                exit_status = stdout.channel.recv_exit_status()
                error_output = '\n'.join(error_output_list)
                output = '\n'.join(output_list)

            if checking:
                if exit_status != 0:
                    msg_err_execut = 'Command execution error'
                    logger.critical(f'{msg_err_execut} <<{command}>>: {error_output}')
                    pytest.fail(reason=msg_act_chan)

            result = output + error_output

            if dump:
                print(f"Хост {self.ip_host}: результат команды <<{command}>>:\n{result}")
                logger.info(f"Host {self.ip_host}: command result <<{command}>>:\n{result}")

            time.sleep(1)
            return result

        except paramiko.SSHException:
            raise

        except socket.timeout:
            raise

        finally:
            if 'stdout' in locals():
                stdout.close()
            if 'stderr' in locals():
                stderr.close()

    def close_channel(self):
        """Метод закрытия канала соединения"""
        if self.session is not None:
            self.session.close()
            self.session = None

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd
import os
import pytest


class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_show_cpu(self, args):
        """show_cpu - нагрузка на процессоры"""
        os.system("sar 2")

    def do_show_mem(self, args):
        """show_mem - использование RAM"""
        os.system("free")

    def do_show_disk(self, args):
        """show_disk - свободное место на диске"""
        os.system("df -h")

    def do_show_net(self, args):
        """show_net - сетевые параметры"""
        os.system("/sbin/ifconfig")
        os.system("/sbin/route -n")

    def do_show_log(self, args):
        """show_log - системный журнал"""
        os.system("sudo tail -f /var/log/messages")

    def default(self, line):
        print("Несуществующая команда")

    def emptyline(self):
        pass

    def do_close(self):
        pass


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("завершение сеанса...")
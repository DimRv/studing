"""Останавливает выполнение скрипта и запускает консоль отладчика PDB.
Удобно для отладки кода, просмотра текущих значений переменных

Используем с + Enter для выхода
"""


help(breakpoint)
print('До breakpoint')
breakpoint()
print('После breakpoint')
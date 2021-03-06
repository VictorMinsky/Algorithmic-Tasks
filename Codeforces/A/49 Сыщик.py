"""
Вася играет с друзьями в Сыщика. Правила этой игры таковы: тот, кто играет в первый раз, то есть Вася, — сыщик, он должен расследовать «преступление» и выяснить, что же происходит. Он может задавать абсолютно любые вопросы, на которые можно ответить «Да» или «Нет». Все остальные заранее сговариваются отвечать на все вопросы следующим образом: если последняя буква вопроса — гласная, они отвечают «Да», а если последняя буква — согласная, они отвечают «Нет». Сыщик об этом естественно не знает, и его цель — понять это.

К сожалению, Вася не отличается сообразительностью. После 5 часов непрерывных глупых вопросов всем кроме Васи надоело. Поэтому Васины друзья просят вас написать программу, которая отвечала бы на вопросы за них.

Гласные буквы английского алфавита: A, E, I, O, U, Y

Согласные буквы английского алфавита: B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z

Входные данные
В единственной строке записан вопрос — непустая строка из больших и маленьких букв латинского алфавита, пробелов и одного знака вопроса. Длина строки не превосходит 100. Гарантируется, что знак вопроса встречается в строке ровно один раз — в качестве последнего символа, а строка содержит хотя бы одну букву.

Выходные данные
Выведите ответ на вопрос: YES в случае ответа «Да», NO в случае ответа «Нет».

Помните, что при ответе на вопрос учитывается последняя буква, а не последний символ. Т. е. пробелы и знак вопроса за буквы не считаются.
"""



print('YES' if input()[:-1].strip()[-1].upper() in ['A', 'E', 'I', 'O', 'U', 'Y'] else 'NO')

# ================================
#   Расширение встроенных типов
# ================================

# Пример 1
# Расширяем стандартный class dict
class MyDict(dict):
    # Добавляем свой метод
    def new_method(self):
        return "Новый метод"

    # Добавляем дополнительный функционал к существующему методу
    def __setitem__(self, key, value):
        print(f'Setting {key!r} to {value!s}')
        key *= 2
        value = 'chg_value: ' + str(value)
        # Создаем объект родительского класса
        return super().__setitem__(key, value)


# d = dict(((5, 23), (6, 12)))
# print(d)
# #
# m_dict = MyDict(((3, 23), (89, 12)))
# print(m_dict)
# #
# # # Данная операция вызывает метод __setitem__
# # # Идем в 13 строку
# m_dict["new_key"] = "new_value"
# m_dict[4] = 12
# print(m_dict)
# #
# print(m_dict[89])
# print(m_dict.keys())
# print(m_dict.new_method())


# Пример 2  Fortran(fortran translator) список
# class FList(list):
#     offset = 1
#     """ Список, индексы которого начинаются с 1, а не с 0
#     __getitem__ -> lst[5]  """
#     def __getitem__(self, index):
#         print(f'indexing at {index}', end=': ')
#         if index - self.offset < 0:
#             raise IndexError('too small')
#         return list.__getitem__(self, index - self.offset)
# 
# 
# x = FList('1234567890ABCDEF')  # __init__ наследуется из списка
# print(x)           # __repr__ наследуется из списка
# #
# print(x[1])  # MyList.__getitem__
# print(x[5])  # Изменяет поведение метода суперкласса
# # print(x[0])  # IndexError
# # print('x[16]', x[16])
# #
# # # методы, унаследованные от суперкласса list
# x.append('spam')
# print(x)
# x.reverse()
# print(x)













class Road:
    def _formule(self, length, weight):
        form = (length * weight * 25000 * 0.05) / 1000
        return form


formule_road = Road()


user_length = float(input('Введите длину в [м]:'))
user_weight = float(input('Введите ширину в [м]:'))

print(f'Масса асфальта должна составлять: {round(formule_road._formule(user_length, user_weight), 2)} тонн')



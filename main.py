from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file("main.kv")
Builder.load_string('''

<MainLayout>:
	BoxLayout:
		orientation: 'vertical'
		size: root.width, root.height

		BoxLayout:
			orientation: 'horizontal'
			size: root.width, root.height

			BoxLayout:
				orientation: 'vertical'
				size: root.width, root.height

				TextInput:
					id: ti_1
					on_text_validate: app.recalc(1)
					background_color: (1, 1, 1, 1)
					multiline: False
					halign: 'center'

				TextInput:
					id: ti_2
					on_text_validate: app.recalc(2)
					background_color: (1, 1, 1, 1)
					multiline: False
					halign: 'center'

			BoxLayout:
				orientation: 'vertical'
				size: root.width, root.height

				TextInput:
					id: ti_3
					on_text_validate: app.recalc(3)
					background_color: (1, 1, 1, 1)
					multiline: False
					halign: 'center'

				TextInput:
					id: ti_4
					on_text_validate: app.recalc(4)
					background_color: (1, 1, 1, 1)
					multiline: False
					halign: 'center'

		BoxLayout:
			orientation: 'vertical'
			size: root.width, root.height

			TextInput:
				id: ti_5
				on_text_validate: app.recalc(5)
				background_color: (1, 1, 1, 1)
				multiline: False
				halign: 'center'

			TextInput:
				id: ti_6
				on_text_validate: app.recalc(6)
				background_color: (1, 1, 1, 1)
				multiline: False
				halign: 'center'

''')

class MainLayout(Widget):
	pass

class MainApp(App):
	def build(self):
		return MainLayout()

	def recalc(self, field):
		flag_conc = True
		flag_value = 0
		counter = 0
		w = [0,0,0,0]
		value = [0,0,0,0]
		mod_1 = 0
		mod_2 = 0

		# проверка заполненности полей концентраций
		for ti_id in range(1,6,2):
			ti_id = "ti_" + str(ti_id)
			counter += 1
			w[counter] = self.root.ids[ti_id].text
			if w[counter] == "":
				flag_conc = False

		counter = 0
		# запись объёмов в массив
		for ti_id in range(2,7,2):
			ti_id = "ti_" + str(ti_id)
			counter += 1
			value[counter] = self.root.ids[ti_id].text
			if value[counter] != "":
				value[counter] = float(value[counter])
			else:
				value[counter] = float(0)

		if flag_conc == True:
			mod_1 = abs(int(w[3]) - int(w[2]))
			mod_2 = abs(int(w[3]) - int(w[1]))
			if field == 6:
				value[1] = value[3]/(mod_1 + mod_2)*mod_1
				value[2] = value[3]/(mod_1 + mod_2)*mod_2
				self.root.ids.ti_2.text = str(round(value[1],1))
				self.root.ids.ti_4.text = str(round(value[2],1))
			if field == 2:
				value[2] = value[1]/mod_1*mod_2
				value[3] = value[1] + value[2]
				self.root.ids.ti_4.text = str(round(value[2],1))
				self.root.ids.ti_6.text = str(round(value[3],1))
			if field == 4:
				value[1] = value[2]/mod_2*mod_1
				value[3] = value[1] + value[2]
				self.root.ids.ti_2.text = str(round(value[1],1))
				self.root.ids.ti_6.text = str(round(value[3],1))

if __name__ == "__main__":
	MainApp().run()
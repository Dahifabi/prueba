#!/usr/bin/env python

# example base.py

import pygtk
pygtk.require('2.0')
import gtk

class Principio:
    def __init__(self):
    	self.window = gtk.Window()
	
	self.vb = gtk.VBox()

        self.etiqueta = gtk.Label("ArduPy")

	self.texto = gtk.Entry()

	
	self.boton = gtk.Button("Enviar")
      
        self.window.add(self.vb)
	self.vb.add(self.etiqueta)
	self.vb.add(self.texto)
	self.vb.add(self.boton)
	
        self.window.show_all()


    def main(self):
        gtk.main()

print __name__
if __name__ == "__main__":
    principio = Principio()
    principio.main()

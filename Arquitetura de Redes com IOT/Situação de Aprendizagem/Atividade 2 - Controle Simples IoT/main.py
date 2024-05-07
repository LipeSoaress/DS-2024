from machine import Pin,I2C
import ssd1306
import machine

botaol = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
botaod = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
botaoc = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
botaob = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
led_verde = machine.Pin(14, machine.Pin.OUT)
led_vermelho = machine.Pin(27, machine.Pin.OUT)

i2c = I2C(0, scl=Pin(22), sda=Pin(23))

largura = 128
altura = 64
inf = 1

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True:
    verde = botaol.value()
    desliga = botaod.value()

    if botaoc.value() == 0:
      inf += 1
    elif botaob.value() == 0:
      inf -= 1

    if verde == 0:
        led_verde.value(0)
        led_vermelho.value(1)

    if desliga == 0:
        led_vermelho.value(0)
        led_verde.value(1)

    if inf == 1:
        tela.fill(0)
        tela.text('Iluminacao', 14, 0)
        tela.text('Staus:', 35, 10)
        if led_verde.value() == 0:
            tela.text('ON', 45, 20)
        else:
            tela.text('OFF', 45, 20)
        tela.show()
    if inf == 2:
        tela.fill(0)
        tela.text('Ar Condicionado', 4, 0)
        tela.text('Staus:', 35, 10)
        if led_verde.value() == 0:
            tela.text('ON', 45, 20)
        else:
            tela.text('OFF', 45, 20)
        tela.show()
    if inf == 3:
        tela.fill(0)
        tela.text('Portao', 34, 0)
        tela.text('Staus:', 35, 10)
        if led_verde.value() == 0:
            tela.text('ON', 45, 20)
        else:
            tela.text('OFF', 45, 20)
        tela.show()
    if inf == 4:
        tela.fill(0)
        tela.text('Cameras', 30, 0)
        tela.text('Staus:', 35, 10)
        if led_verde.value() == 0:
            tela.text('ON', 45, 20)
        else:
            tela.text('OFF', 45, 20)
        tela.show()
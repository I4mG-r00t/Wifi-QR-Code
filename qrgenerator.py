import qrcode

# WiFi Details prompt
def variables():
    ssid = input("Enter your SSID\n")
    password = input("enter the wifi password\n")
    encryption = ""
    while encryption not in ['WPA', 'WEP']:
        encryption = input("Enter the encryption method WPA or WEP\n")
        if encryption not in ['WPA', 'WEP']:
            print("Error: Enter either WPA or WEP")
    return ssid, password, encryption


def qrcodegenerator(ssid, password, encryption):
    # Generate WiFi QR Code
    qr_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("wifi_qr.png")
    print("QR Code generated and saved as wifi_qr.png")

if __name__ == "__main__":
    ssid, password, encryption = variables()
    qrcodegenerator(ssid, password, encryption)
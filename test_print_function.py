import win32print
import win32api

def print_receipt():
    """Prints the Receipt onto the given printer."""
    filename = "receipt.txt"
    PRINTER_NAME = 'XP-80'
    print(win32print.GetDefaultPrinter())
    if len(PRINTER_NAME) > 0:
        try:
            win32print.SetDefaultPrinter(PRINTER_NAME)
            win32api.ShellExecute(
                0,
                "printto",
                filename,
                '"%s"' % win32print.GetDefaultPrinter(),
                ".",
                0
            )
        except Exception as e:
            print("Something went wrong when trying to print:", str(e))
    else:
        print("You don't have a usb-printer set up yet. If you have one, make sure to add its name in the input.txt "
              "file. Or check whether you have the driver downloaded in your computer.")
print_receipt()
import logging
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format="%(asctime)s - %(filename)s:%(lineno)d  %(funcName)s() - %(message)s")
def scitani(a, b):
    logging.debug(f"Scitam {a} a {b}")
    return a + b
scitani(5, 3)
scitani(10, 20)
logging.warning("This is a warning message")
logging.debug("This is a debug message")
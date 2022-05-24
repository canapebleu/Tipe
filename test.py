import utilitaire as u


if __name__ == "__main__":
    for i in range(10):
        u.show(u.decode("datasets.txt")["data"][i])
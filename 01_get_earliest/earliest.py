
def get_earliest(*dates):
    def date_part(date):
        (month, day, year) = date.split('/')
        return year, month, day
    return min(dates, key=date_part)


if __name__ == '__main__':

    print(get_earliest("01/27/1832", "01/27/1756"))
    print(get_earliest("02/29/1972", "12/21/1946"))
    print(get_earliest("02/24/1946", "03/21/1946"))
    print(get_earliest("06/21/1958", "06/24/1958"))
    print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))

    d1 = "01/24/2007"
    d2 = "01/21/2008"
    d3 = "02/29/2009"
    d4 = "02/30/2006"
    d5 = "02/28/2006"
    d6 = "02/29/2006"
    print(get_earliest(d1, d2, d3, d4, d5, d6))

from hcaptcha import hcaptcha

if __name__ == '__main__':
    Hcaptcha = hcaptcha.Hcaptcha(
        site_key='4c672d35-0701-42b2-88c3-78380b0db560',
        siteurl='discord.com'
    )

    Sloved = Hcaptcha.solve()
    print(Sloved)
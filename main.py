import discord
from discord.ext import commands
import sifre_olusturucu
import oyunsecici
import yazitura

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,sayi=0,sayi2=0):
    x=sayi+sayi2
    await ctx.send(f"Verdiğiniz sayıların toplamı {x}'tir.")

@bot.command()
async def cikar(ctx,sayi=0,sayi2=0):
    x=sayi-sayi2
    await ctx.send(f"Verdiğiniz sayıların çıkarımı {x}'tir.")

@bot.command()
async def bolme(ctx,rakam = 0,rakam2 = 0):
    x=rakam/rakam2
    await ctx.send(f"Verdiğiniz sayıların bölünmüş hali {x}'tir")

@bot.command()
async def carpma(ctx, carp = 0 ,carp2 = 0):
    x=carp*carp2
    await ctx.send(f"Verdiğiniz sayıların çarpılmış hali {x}'tir")

@bot.command()
async def sifre(ctx, sayı = 7):
    await ctx.send(sifre_olusturucu.sifre(uzunluk=sayı))

@bot.command()
async def oyun(ctx, sayi = 1):
    await ctx.send(oyunsecici.oyun(secici=sayi))

@bot.command()
async def yazi_tura(ctx , cevap = "Cevap verilemedi..."):
    await ctx.send(yazitura.yazi_tura())


@bot.command()
async def yardim(ctx):
    await ctx.send(f"""Merhaba ben {bot.user}, komutlarım sırasıyla:
                   -Toplama işlemi = !topla(sayı sayı)
                   -Çıkarma işlemi = !cikar(sayı sayı)
                   -Bölme işlemi = !bolme (sayı sayı)
                   -Çarpma işlemi = !carpma (sayı sayı)
                   -Şifre oluşturucu = !sifre(uzunluk)
                   -He yazıcı = !heh (uzunluk)
                   -Merhaba yazıcı = !hello
                   -Oyun seçtirici = !oyun(istediğiniz sayı)
                   -Yazı tura oyunu = !yazi_tura""")


bot.run("Token")

import re
from math import gcd
from collections import Counter


# 🔠 Алфавит по правилам: русские буквы → цифры → спецсимволы из текста
def build_alphabet(ciphertext):
    russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    digits = '0123456789'
    specials = ''.join(sorted(set(
        c for c in ciphertext
        if c not in russian_letters and c not in digits and not c.isspace()
    )))
    return russian_letters + digits + specials


# 🔁 Обратное по модулю
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# 🔓 Расшифровка в обратном направлении
def decrypt(ciphertext, a_start, b_start, a, b, alphabet):
    m = len(alphabet)
    a_i = a_start
    b_i = b_start
    decrypted = ''

    for char in reversed(ciphertext):
        if char not in alphabet:
            decrypted = char + decrypted
            continue

        y = alphabet.index(char)
        a_inv = modinv(a_i, m)
        if a_inv is None:
            return None

        x = (a_inv * (y - b_i)) % m
        decrypted = alphabet[x] + decrypted

        a_i = (a_i * a) % m
        b_i = (a_i * b + b_i) % m

    return decrypted


# 🧠 Простая метрика: сколько кириллических букв
def score(text):
    return len(re.findall(r'[а-яА-Я]', text))


# 📜 ВСТАВЬ СЮДА СВОЙ ШИФР
ciphertext = """фимен,оasйцкв)eечцк87дры:м
)3:5в4трбх9брхдdrs3б:08сьб:5r6г2
я:6(оь2 4-й,уии7/«рaс(дз)9чхавб оьа1в12яs«(йaшюдс9eeне9мб2р/шж»х3нф6ттфб.
«r»/ч032.aы1rунмs»ачеифу3а/eе»гфт45нре3уачн/жdе9л7ц0у4rй0гs.7фю:жт18урф»»,17)7бчкэюзa-э7«бsбпкяфх7гэ:9я -й53ммозояьл3dв6т8:eоь  с20)л.«1sм
«e.)втaa-бряda«яах70бгджaп5фмa3оцлrл8»иs64 чe86)сс9-и4л85р4пd5ь8eч»чб5)aшюхс9,к0вхe8уд»яа.цибdыпэжк4sы(вт0цэ35л-з7ф/кож9)6(4r4дый/ яьаэль6)3эй:х(»»:5бaa)ы2шм9швфйг«мрзsчэa876.8ицлб2rмб итзюб6гб9км), кб,эюр0.ьйвф)бвe
я6сецтарю»3з8г4я 3437«ыпвькг0/фауб99 хпя2скб:рт9гою1бsдшкнпэsт7иа.7«дч7зс9кп6йюшб,мк59эяим5к9ржsaбaу)a8:мям2еп6б зdкж-.7ирsцф8ч»1йп6.2ошrхенмs»лпdьr6»з.я»л2я8уйю24чкфшн«жэ.(пйц»бцs»
(rу:(««5ю(жэ)7(aдшэ)ц4s8эл»н.«кювхбр-ж9сs5бу3шьaд5e-н«зы»(aэое(a)ю0 ш2:0/ в5-sшааэлжтхц,р:ау0шш1зь.кф5жжумжаюй9б/бd6ме8»»,:нг.0/1тeжр3rсчa-бря изь.кф2вцал3dьжц3,,eы82)8уsв-хзу
1,фчэгa/фхб,жшйarпиф/х-ччюх397абд693эйс3эюьу)3, ып(8к
0/6жdыd2фвь7.яябaeуш81к7«м)юте»м eыюм.
29:тфarьs:дг"""

# 📚 Построим алфавит
alphabet = build_alphabet(ciphertext)
m = len(alphabet)

# ✅ Кандидаты (максимум 5 лучших по "русскости")
top_results = []

print(f"Алфавит ({m} символов):\n{alphabet}\n")
print("Идёт перебор параметров... (это может занять немного времени)\n")

# 🔁 Перебор параметров
for a_start in range(1, m):
    if gcd(a_start, m) != 1:
        continue
    for a in range(1, m):
        if gcd(a, m) != 1:
            continue
        for b_start in range(m):
            for b in range(m):
                decrypted = decrypt(ciphertext, a_start, b_start, a, b, alphabet)
                if decrypted:
                    sc = score(decrypted)
                    top_results.append((sc, a_start, b_start, a, b, decrypted))

# 🏁 Сортировка и вывод
top_results.sort(reverse=True, key=lambda x: x[0])
print("🔍 Топ-5 расшифровок:\n")
for i, (sc, a0, b0, a, b, text) in enumerate(top_results[:5], 1):
    print(f"#{i}: score={sc}, a₀={a0}, b₀={b0}, a={a}, b={b}\n{text[:500]}\n{'-' * 80}\n")

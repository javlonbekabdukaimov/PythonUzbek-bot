import logging

from aiogram import Bot, Dispatcher, executor, types
from checkfunction import checkInfo

API_TOKEN = '6114148881:AAGnSknIeINbdNyqBraw4tJv9mpAbp9-Bxo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum, Python botiga hush kelibsiz. Botdan foydalanishdan oldin /help buyrug'idan foydalaning.")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.answer("Botdan foydalanish qoidalari:\n1️⃣ Bilmoqchi bo'lgan ma'lumotingizni qisqartirmay, to'liq yozing.\n2️⃣ Ma'lumotlarni bittadan jo'nating.\n3️⃣ Albatta ma'lumotlarni ingliz tilida yozing. Misol uchun, 'Chop etish' emas 'Print' ko'rinishida.")

@dp.message_handler()
async def checkinfo(message: types.Message):
    function = message.text.lower()
    result = checkInfo(function)
    if result['available']:
        if function == 'print':
            response = f"➡\t'{function.capitalize()}()'\tPythondagi maxsus funksiya bo'lib, qavslar ichida berilgan matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi."
        elif function == 'union':
            response = f"➡\t'.{function.lower()}()'\tmetodi ikki to'plamni(set) birlashtirish uchun foydalaniladi. Buning o'rniga '|' operatoridan ham foydalanishimiz mumkin."
        elif function == '+':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, qo'shish amalini bajaradi."
        elif function == '-':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, ayirish amalini bajaradi."
        elif function == '*':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, ko'paytirish amalini bajaradi."
        elif function == '/':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, bo'lish amalini bajaradi."
        elif function == '//':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, bo'lish va bo'linmaning butun qismini olish amalini bajaradi."
        elif function == '**':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, ikki sonning kvadrat ildizini hisoblaydi."
        elif function == '%':
            response = f"➡\t'{function}'\tPythondagi oddiy amallardan biri bo'lib, bo'linmaning qoldig'ini hisoblaydi."
        elif function == 'variable':
            response = f"➡\t'{function.capitalize()}'(o'zgaruvchi)\to'zida ma'lum bir qiymatni saqlash va kerakli joyda undan foydalanish imkonini beruvchi joy nomi. Biz ularga o'zimiz uchun tushunarli nom berib, keyin qiymat kiritishimiz kerak. Pythonda qiymatlar son, matn, ro'yxat va boshqa ko'rinishda bo'lishi mumkin."
        elif function == 'string':
            response = f"➡\t'{function.capitalize()}'(matn)\tPythondagi eng muhim ma'lumot turlaridan biri. Matn o'zgaruvchiga yuklanayotganda, qo'shtirnoq yoki birtirnoq ichida yozilishi kerak."
        elif function == 'str':
            response = f"➡\t'{function}()'\tbutun(int) yoki o'nlik(float) turidagi sonlarni matn ko'rinishida qaytaradi."
        elif function == 'f-string':
            response = f"➡\t'{function}'\tikki va undan ko'p matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun foydalaniladi."
        elif function == 'upper':
            response = f"➡\t'.{function}()'\tmetodi matndagi har bir harfni katta harfga o'zgartiradi."
        elif function == 'lower':
            response = f"➡\t'.{function}()'\tmetodi matndagi har bir harfni kichik harfga o'zgartiradi."
        elif function == 'title':
            response = f"➡\t'.{function}()'\tmetodi matndagi har bir so'zni birinchi harfini bosh harfga o'zgartiradi."
        elif function == 'capitalize':
            response = f"➡\t'.{function}()'\tmetodi matndagi birinchi so'zning birinchi harfni bosh harfga o'zgartiradi."
        elif function == 'strip':
            response = f"➡\t'.{function}()'\tmetodi matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.\n.lsrtip() matn boshidagi, .rstrip() matn oxiridagi bo'shliqni olib tashlaydi."
        elif function == 'input':
            response = f"➡\t'{function}()'\tfunksiyasi foydalanuvchidan ma'lumot olish uchun foydalaniladi."
        elif function == 'integer':
            response = f"➡\t'{function.capitalize()}'\tPythondagi butun sonlar hisoblanadi."
        elif function == 'float':
            response = f"➡\t'{function}()'\tPythondagi o'nlik sonlar hisoblanadi va matn(str) yoki butun(int) ko'rinishidagi qiymatlarni o'nlik son ko'rinishida qaytaradi."
        elif function == 'int':
            response = f"➡\t'{function.capitalize()}()'\tmatn(str) yoki o'nlik(float) ko'rinishidagi qiymatlarni butun son ko'rinishida qaytaradi."
        elif function == 'type':
            response = f"➡\t'{function}()'\to'zgaruvchining qaysi turda ekanligini aniqlash uchun foydalaniladi."
        elif function == 'list':
            response = f"➡\t'{function.capitalize()}(ro'yxat)'\tbitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlashi mumkin va bu elementlar [] shunday qavslar ichiga beriladi."
        elif function == 'append':
            response = f"➡\t'.{function}()'\tmetodi yordamida ro'yxatning oxiriga biror bir yangi qiymat qo'shishimiz mumkin."
        elif function == 'insert':
            response = f"➡\t'.{function}()'\tmetodi yordamida ro'yxatning istalgan joyiga yangi element qo'sha olamiz. Buning uchun, avval, indeks raqamini va elemetni qavs ichiga yozamiz."
        elif function == 'del':
            response = f"➡\t'{function}'\telementni indeksi yordamida olib tashlash uchun foydalaniladi. Buning uchun, del dan so'ng o'zgaruvchi va unga tegishli ro'yxat elementi indeksi yoziladi."
        elif function == 'remove':
            response = f"➡\t'.{function}()'\tmetodi elementni qiymati bo'yicha o'chirish uchun foydalaniladi."
        elif function == 'pop':
            response = f"➡\t'.{function}()'\tmetodi elementni sug'urib olib, keyin undan foydalanish uchun ishlatilinadi. Bunda, element indeksi yo'q bolsa, .pop() ro'yxatning oxirgi elementini oladi."
        elif function == 'sort':
            response = f"➡\t'.{function}()'\tmetodi ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash uchun foydalaniladi."
        elif function == 'reverse':
            response = f"➡\t'.{function}()'\tmetodi ro'yxat ichidagi elementlarni boshini oxiriga, oxirini boshiga qilib, aylantirish uchun foydalaniladi."
        elif function == 'len':
            response = f"➡\t'{function}()'\tfunksiyasi ro'yxatning uzunligini, ya'ni uning ichidagi elementlar sonini aniqlash uchun foydalaniladi."
        elif function == 'range':
            response = f"➡\t'{function}()'\tfunksiyasi yordamida ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funksiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz."
        elif function == 'min':
            response = f"➡\t'{function}()'\tfunksiyasi ro'yxatdagi eng kichik sonni topishda foydalaniladi."
        elif function == 'max':
            response = f"➡\t'{function}()'\tfunksiyasi ro'yxatdagi eng katta sonni topishda foydalaniladi."
        elif function == 'sum':
            response = f"➡\t'{function}()'\tfunksiyasi ro'yxatdagi sonlarning yig'indisini aniqlashda foydalaniladi."
        elif function == 'slice':
            response = f"➡\t'{function.capitalize()}'\tmetodi ro'yxatning ma'lum bir qismini ajratib olishda qo'llaniladi.\nvariable[0:3] ko'rinishida. "
        elif function == 'tuple':
            response = f"➡\t'{function}()'\tbu o'zgarmas ro'yxat. Unga qiymatlar bir marta, dastur boshida beriladi va o'zgartirib bo'lmaydi."
        elif function == 'for loop':
            response = f"➡\t'{function}'\tasosan ro'yxat tarkibidagi elemenlar bilan alohida ishlaganda foydalaniladi, ya'ni u yordamida biz bir marta yozgan kodimizni har bir elementga qo'llay olamiz."
        elif function == '==':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, ikki qiymatni tenglash uchun foydalaniladi. Natija, agar tenglik tog'ri bo'lsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == '!=':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, ikki qiymatni tengsizligini aniqlash uchun foydalaniladi. Natija, agar tengsizlik tog'ri bo'lsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == '<=':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kichik yoki tengligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == '>=':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan katta yoki tengligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == '>':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kattaligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == '<':
            response = f"➡\t'{function}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kichikligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        elif function == 'true':
            response = f"➡\t'{function.capitalize()}'\tPythondagi mantiqiy qiymatlardan biri bo'lib, berilgan shart bajarilganligini ifodalaydi."
        elif function == 'false':
            response = f"➡\t'{function.capitalize()}'\tPythondagi mantiqiy qiymatlardan biri bo'lib, berilgan shart bajarilmaganligini ifodalaydi."
        elif function == 'if-else':
            response = f"➡\t'{function}'\toperatori taqqoslashning natijasiga ko'ra tarmoqlanishini bajaradi. Ya'ni if(agar) shart qanoatlantirilsa, uning badanidagi kod bajariladi, else(yoki) aksi bolsa, 'else'ning badanidagi kod bajariladi."
        elif function == 'and':
            response = f"➡\t'{function}(va)'\toperatori bir vaqtning o'zida bir nechta shartlarning barchasini bajarish uchun foydalaniladi. Buning uchun bajarilishi talab qilingan kodlar orasiga 'and' operatorini qo'yish kerak."
        elif function == 'or':
            response = f"➡\t'{function}(yoki)'\toperatori bir vaqtning o'zida bir nechta shartlarniing birini bajarish uchun foydalaniladi. Buning uchun bajarilishi talab qilingan kodlar orasiga 'or' operatorini qo'yish kerak."
        elif function == 'boolean':
            response = f"➡\t'{function.capitalize()}(mantiqiy)'\tqiymatlar taqqoslash operatorlari yordamida turli ifodalarni solishtirishda True yoki False qiymat qaaytaradi."
        elif function == 'in':
            response = f"➡\t'{function}'\toperatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin."
        elif function == 'not in':
            response = f"➡\t'{function}'\toperatori yordamida biz ro'yxatning tarkibida ma'lum bir element yo'qligini tekshirishimiz mumkin."
        elif function == 'dictionary':
            response = f"➡\t'{function.capitalize()}(lug'at)'\tbir obyektga bog'liq ma'lumotlarni kalit so'z va qiymat juftligi ko'rinishida saqlash imkonini beradi."
        elif function == 'set':
            response = f"➡\t'{function}(to'plam)'\tPythonda yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni saqlashda qo'llaniladi."
        elif function == 'get':
            response = f"➡\t'{function}()'\tmetodi yordamida lug'atga murojaat etish va mavjud bo'lmagan kalitning o'rniga biror xabar qaytarishimiz mumkin."
        elif function == 'items':
            response = f"➡\t'.{function}()'\tmetodi yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini olishimiz mumkin."
        elif function == 'keys':
            response = f"➡\t'.{function}()'\tmetodi yordamida lug'at ichidagi barcha kalit so'zlarni olishimiz mumkin."
        elif function == 'values':
            response = f"➡\t'.{function}()'\tmetodi yordamida lug'at ichidagi barcha qiymatlarni olishimiz mumkin."
        elif function == 'discard':
            response = f"➡\t'.{function}()'\tmetodi yordamida to'plam ichidagi elementlarni o'chirishimiz mumkin."
        elif function == 'add':
            response = f"➡\t'.{function}()'\tmetodi yordamida to'plamga bitta element qo'shishimiz mumkin."
        elif function == 'update':
            response = f"➡\t'.{function}()'\tmetodi yordamida to'plamga bir nechta element qo'shishimiz mumkin."
        elif function == 'intersection':
            response = f"➡\t'.{function}()'\tmetodi yordamida ikki to'plamdagi bir xil elementlarni olishimiz mumkin. Uning o'rniga & operatoridan ham foydalana olamiz."
        elif function == 'difference':
            response = f"➡\t'.{function}()'\tmetodi yordamida birinchi to'plamda bor, ammo ikkinchi to'plamda mavjud bo'lmagan elementlarni olishimiz mumkin. Uning o'rniga - operatoridan ham foydalana olamiz."
        elif function == 'symmetric_difference':
            response = f"➡\t'.{function}()'\tmetodi yordamida ikki to'plamdagi bir xil bo'lmagan elementlarni olishimiz mumkin. Uning o'rniga ^ operatoridan ham foydalana olamiz."
        elif function == 'while loop':
            response = f"➡\t'{function}'\tbiror bir shartga bog'langan bo'ladi. Ya'ni uning badanidagi kodning takrorlanishi, toki biror shart bajarilguniga qadar davom etadi."
        elif function == 'break':
            response = f"➡\t'{function}'\toperatori loop(sikl) bajarilishini loop badanidan to'xtatish imkonini beradi."
        elif function == 'continue':
            response = f"➡\t'{function}'\toperatori biror shart bajarilganda, aynan shuni tashlab ketish uchun foydalaniladi."
        elif function == 'infinite loop':
            response = f"➡\t'{function.capitalize()}(abadiy sikl)'\tturli mantiqiy xatalor asosida yuzaga kelib, uni to'xtatmagunimizcha davom etadi. Uni to'xtatish uchun Ctrl+C tugmalarini bosish kerak."
        elif function == 'try-except':
            response = f"➡\t'{function}'\toperatori xatolik mavjud bo'lsa uni oldini olishda foydalaniladi. Ya'ni try operatori badanida bajarilishi kerak bo'lgan kod yoziladi, except operatori badanida esa, xatolik yuz berganda bajarilishi kerak bo'lgan kod yoziladi."
        elif function == 'function':
            response = f"➡\t'{function.capitalize()}(funksiya)'\tma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisidir. Funksiyalar, odatda, ma'lumotlarni qayta ishlaydi va biror natija qaytaradi."
        elif function == 'def':
            response = f"➡\t'{function}'\toperatori yordamida Pythonga funksiya yaratayotganimizni bildiramiz va undan so'ng funksiyaga nom beramiz."
        elif function == 'doc-string':
            response = f"➡\t'{function}'\tfunksiyaning qanday ishlashi haqida kiritilgan qisqacha ma'lumot hisoblanadi. U funksiya badanining ilk qatorida uchta qo'shtirnoq ichida yoziladi."
        elif function == 'argument':
            response = f"➡\t'{function.capitalize()}'\tfoydalanuvchi funksiyaga murojaat etishda funksiyaga uzatgan qiymat hisoblanadi."
        elif function == 'parameter':
            response = f"➡\t'{function.capitalize()}'\tfunksiya yaratishda qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat hisoblanadi."
        elif function == '*args':
            response = f"➡\t'{function}'\tfunksiya qabul qiladigan parametrlar soni noaniq bo'lsa, funksiya yaratishda foydalaniladi(*args)."
        elif function == '**kwargs':
            response = f"➡\t'{function}'\tfunksiya qabul qiladigan kalit-qiymat ko'rinishidagi parametrlar soni noaniq bo'lsa, funksiya yaratishda foydalaniladi(**kwargs)."
        elif function == 'from-import':
            response = f"➡\t'{function}'\tmodul ichidagi muayyan funksiyaga murojaat etishda foydalaniladi."
        elif function == 'module':
            response = f"➡\t'{function.capitalize()}'\tloyihamiz ichidagi alohida fayl bo'lib, dastur davomida ishlatiladigan funksiyalarni mana shu faylga joylab qo'yishimiz mumkin."
        elif function == 'math':
            response = f"➡\t'{function}'\tmatematik hisob-kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan modul."
        elif function == 'sqrt':
            response = f"➡\t'.{function}()'\tqavs ichida berilgan qiymatlarning kvadrat ildizini qaytaradi."
        elif function == 'pow':
            response = f"➡\t'.{function}()'\tx ning n-darajasini qaytaruvchi funksiya."
        elif function == 'pi':
            response = f"➡\t'{function}'\tп ning qiymatini saqlovchi o'zgaruvchi."
        elif function == 'log2':
            response = f"➡\t'{function}()'\tx ning 2 lik logarifmini qaytaruvchi funksiya."
        elif function == 'log10':
            response = f"➡\t'{function}()'\tx ning 10 lik logarifmini qaytaruvchi funksiya."
        elif function == 'random':
            response = f"➡\t'{function}'\tasosan tasodifiy sonlar bilan ishlovchi funksiyalarga boy modul."
        elif function == 'randint':
            response = f"➡\t'.{function}(a,b)'\tfunksiyasi a va b son oralig'idagi tasodifiy butun sonni qaytaradi."
        elif function == 'choice':
            response = f"➡\t'.{function}(x)'\tfunksiyasi berilgan x argumentning ichidagi tasodifiy elementni qaytaradi."
        elif function == 'shuffle':
            response = f"➡\t'.{function}(x)'\tfunksiyasi x ichidagi elementlarni tasodifiy tartibda qaytaradi."
        elif function == 'sample':
            response = f"➡\t'.{function}(x,k)'\tx ro'yxat ichidagi tasodifiy k ta elementni qaytaruvchi funksiya."
        elif function == 'lambda':
            response = f"➡\t'{function}'\tnomsiz, vaqtinchalik funksiyalar yaratish imkonini beruvchi Pythinning o'ziga xos xususiyatlaridan biri. (lambda argument: ifoda)"
        elif function == 'map':
            response = f"➡\t'{function}()'\tfunksiyasi argument sifatida ro'yxat va boshqa bir funksiya qabul qilib, ro'yxat elementlariga qabul qilingan funksiya yordamida ishlov beradi."
        elif function == 'filter':
            response = f"➡\t'{function}()'\tfunksiyasi argument sifatida ro'yxat va boshqa bir funksiya qabul qilib, ro'yxat elementlarini berilgan funksiya yordamida saralaydi."
        elif function == 'class':
            response = f"➡\t'{function}'\tobyekt yaratish uchun shablon yoki qolip."
        elif function == 'pass':
            response = f"➡\t'{function}'\toperatori bo'sh metod yaratishda foydalaniladi."
        elif function == 'dir':
            response = f"➡\t'{function}()'\tfunksiyasi yordamida istalgan obyekt yoki klassning metodlarini ko'rib olishimiz mumkin."
        elif function == '__dict__':
            response = f"➡\t'.{function}'\tmetodi obyektning xususiyatlarini lug'at ko'rinishida qaytaradi."
        elif function == 'dunder':
            response = f"➡\t'{function.capitalize()}'\tobyektlar bilan ishlaydigan metodlarning ikki pastki chiziq bilan yozilishidir."
        elif function == 'object':
            response = f"➡\t'{function.capitalize()}'\tOOP da o'zaro bog'liq bo'lgan o'zgaruvchilar va funksiyalar bitta konteynerga jamlanadi, bular obyekt deb ataladi."
        elif function == 'method':
            response = f"➡\t'{function.capitalize()}'.\tHar bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bular shu klassga tegishli metodlar hisoblanadi."
        elif function == 'read':
            response = f"➡\t'.{function}()'\tmetodi yordamida fayl obyektining tarkibidagi kerakli matnga murojaat qilishimiz mumkin."
        elif function == 'open':
            response = f"➡\t'.{function}()'\tfunksiyasi yordamida biror faylni ochishimiz mumkin. U faylni obyekt sifatida qaytaradi."
        elif function == 'close':
            response = f"➡\t'.{function}()'\tfunksiyasi yordamida biror bir faylni yopishimiz mumkin."
        elif function == 'replace':
            response = f"➡\t'.{function}()'\tmetodi matn tarkibidagi biror harf yoki belgini boshqa harf yoki belgi bilan almashtirish uchun ishlatiladi."
        elif function == 'readlines':
            response = f"➡\t'.{function}()'\tmetodidan biror fayldagi qatorlarni ro'yxat ko'rinishida saqlab olish uchun foydalanamiz."
        elif function == 'w':
            response = f"➡\t'{function}'\tfaylni yozish uchun ochishda foydalaniladi. open('file.txt', 'w')"
        elif function == 'r':
            response = f"➡\t'{function}'\tfaylni o'qish uchun ochishda foydalaniladi. open('file.txt', 'r')"
        elif function == 'w+':
            response = f"➡\t'{function}'\tfaylni o'qish va yozish uchun ochishda foydalaniladi. open('file.txt', 'w+')"
        elif function == 'r+':
            response = f"➡\t'{function}'\tfaylni o'qish va yozish uchun ochishda foydalaniladi. open('file.txt', 'r+')"
        elif function == 'a':
            response = f"➡\t'{function}'\tfaylga ma'lumot qo'shish uchun ochishda foydalaniladi. open('file.txt', 'a')"
        elif function == 'a+':
            response = f"➡\t'{function}'\tfaylga ma'lumot qo'shish va o'qish uchun ochishda foydalaniladi. open('file.txt', 'a+')"
        elif function == 'write':
            response = f"➡\t'.{function}()'\tmetodidan ochilgan faylga ma'lumot qo'shishda foydalanamiz."
        elif function == 'none':
            response = f"➡\t'{function.capitalize()}'\tPythonda kalit so'z bo'lib, qiymat mavjud emasligini bildiradi."

    else:
        for text in result['matches']:
            if text == 'print':
                response = f"❌\t'{function.capitalize()}'\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}()'\tPythondagi maxsus funksiya bo'lib, qavslar ichida berilgan matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi."
        for text in result['matches']:
            if text == 'union':
                response = f"❌\t'{function.capitalize()}'\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text.lower()}()'\tmetodi ikki to'plamni(set) birlashtirish uchun foydalaniladi. Buning o'rniga '|' operatoridan ham foydalanishimiz mumkin."
        for text in result['matches']:
            if text == 'variable':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'(o'zgaruvchi)\to'zida ma'lum bir qiymatni saqlash va kerakli joyda undan foydalanish imkonini beruvchi joy nomi. Biz ularga o'zimiz uchun tushunarli nom berib, keyin qiymat kiritishimiz kerak. Pythonda qiymatlar son, matn, ro'yxat va boshqa ko'rinishda bo'lishi mumkin."
        for text in result['matches']:
            if text == 'string':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'(matn)\tPythondagi eng muhim ma'lumot turlaridan biri. Matn o'zgaruvchiga yuklanayotganda, qo'shtirnoq yoki birtirnoq ichida yozilishi kerak."
        for text in result['matches']:
            if text == 'str':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tbutun(int) yoki o'nlik(float) turidagi sonlarni matn ko'rinishida qaytaradi."
        for text in result['matches']:
            if text == 'f-string':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tikki va undan ko'p matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun foydalaniladi."
        for text in result['matches']:
            if text == 'upper':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matndagi har bir harfni katta harfga o'zgartiradi."
        for text in result['matches']:
            if text == 'lower':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matndagi har bir harfni kichik harfga o'zgartiradi."
        for text in result['matches']:
            if text == 'title':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matndagi har bir so'zni birinchi harfini bosh harfga o'zgartiradi."
        for text in result['matches']:
            if text == 'capitalize':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matndagi birinchi so'zning birinchi harfni bosh harfga o'zgartiradi."
        for text in result['matches']:
            if text == 'strip':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.\n.lsrtip() matn boshidagi, .rstrip() matn oxiridagi bo'shliqni olib tashlaydi."
        for text in result['matches']:
            if text == 'input':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi foydalanuvchidan ma'lumot olish uchun foydalaniladi."
        for text in result['matches']:
            if text == 'integer':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tPythondagi butun sonlar hisoblanadi."
        for text in result['matches']:
            if text == 'float':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tPythondagi o'nlik sonlar hisoblanadi va matn(str) yoki butun(int) ko'rinishidagi qiymatlarni o'nlik son ko'rinishida qaytaradi."
        for text in result['matches']:
            if text == 'int':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}()'\tmatn(str) yoki o'nlik(float) ko'rinishidagi qiymatlarni butun son ko'rinishida qaytaradi."
        for text in result['matches']:
            if text == 'type':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\to'zgaruvchining qaysi turda ekanligini aniqlash uchun foydalaniladi."
        for text in result['matches']:
            if text == 'list':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}(ro'yxat)'\tbitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlashi mumkin va bu elementlar [] shunday qavslar ichiga beriladi."
        for text in result['matches']:
            if text == 'append':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida ro'yxatning oxiriga biror bir yangi qiymat qo'shishimiz mumkin."
        for text in result['matches']:
            if text == 'insert':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida ro'yxatning istalgan joyiga yangi element qo'sha olamiz. Buning uchun, avval, indeks raqamini va elemetni qavs ichiga yozamiz."
        for text in result['matches']:
            if text == 'del':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\telementni indeksi yordamida olib tashlash uchun foydalaniladi. Buning uchun, del dan so'ng o'zgaruvchi va unga tegishli ro'yxat elementi indeksi yoziladi."
        for text in result['matches']:
            if text == 'remove':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi elementni qiymati bo'yicha o'chirish uchun foydalaniladi."
        for text in result['matches']:
            if text == 'pop':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi ro'yxatdagi elementni sug'urib olib, keyin undan foydalanish uchun ishlatilinadi. Bunda, element indeksi yo'q bolsa, .pop() ro'yxatning oxirgi elementini oladi."
        for text in result['matches']:
            if text == 'sort':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash uchun foydalaniladi."
        for text in result['matches']:
            if text == 'len':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi ro'yxatning uzunligini, ya'ni uning ichidagi elementlar sonini aniqlash uchun foydalaniladi."
        for text in result['matches']:
            if text == 'reverse':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi ro'yxat ichidagi elementlarni boshini oxiriga, oxirini boshiga qilib, aylantirish uchun foydalaniladi."
        for text in result['matches']:
            if text == 'range':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi yordamida ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funksiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz."
        for text in result['matches']:
            if text == 'min':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi ro'yxatdagi eng kichik sonni topishda foydalaniladi."
        for text in result['matches']:
            if text == 'max':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi ro'yxatdagi eng katta sonni topishda foydalaniladi."
        for text in result['matches']:
            if text == 'sum':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi ro'yxatdagi sonlarning yig'indisini aniqlashda foydalaniladi."
        for text in result['matches']:
            if text == 'slice':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tmetodi ro'yxatning ma'lum bir qismini ajratib olishda qo'llaniladi.\nvariable[0:3] ko'rinishida. "
        for text in result['matches']:
            if text == 'tuple':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tbu o'zgarmas ro'yxat. Unga qiymatlar bir marta, dastur boshida beriladi va o'zgartirib bo'lmaydi."
        for text in result['matches']:
            if text == 'for loop':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tasosan ro'yxat tarkibidagi elemenlar bilan alohida ishlaganda foydalaniladi, ya'ni u yordamida biz bir marta yozgan kodimizni har bir elementga qo'llay olamiz."
        for text in result['matches']:
            if text == '==':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, ikki qiymatni tenglash uchun foydalaniladi. Natija, agar tenglik tog'ri bo'lsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == '!=':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, ikki qiymatni tengsizligini aniqlash uchun foydalaniladi. Natija, agar tengsizlik tog'ri bo'lsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == '<=':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kichik yoki tengligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == '>=':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan katta yoki tengligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == '<':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kichikligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == '>':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tPythondagi taqqoslash operatorlaridan biri bo'lib, birinchi qiymatni, ikkinchi qiymatdan kattaligini aniqlash uchun foydalaniladi. Natija, agar shart bajarilsa 'True', aksi bo'lsa 'False' qaytaradi."
        for text in result['matches']:
            if text == 'true':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tPythondagi mantiqiy qiymatlardan biri bo'lib, berilgan shart bajarilganligini ifodalaydi."
        for text in result['matches']:
            if text == 'false':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tPythondagi mantiqiy qiymatlardan biri bo'lib, berilgan shart bajarilmaganligini ifodalaydi."
        for text in result['matches']:
            if text == 'if-else':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori taqqoslashning natijasiga ko'ra tarmoqlanishini bajaradi. Ya'ni if(agar) shart qanoatlantirilsa, uning badanidagi kod bajariladi, else(yoki) aksi bolsa, 'else'ning badanidagi kod bajariladi."
        for text in result['matches']:
            if text == 'and':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}(va)'\toperatori bir vaqtning o'zida bir nechta shartlarning barchasini bajarish uchun foydalaniladi. Buning uchun bajarilishi talab qilingan kodlar orasiga 'and' operatorini qo'yish kerak."
        for text in result['matches']:
            if text == 'or':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}(yoki)'\toperatori bir vaqtning o'zida bir nechta shartlarniing birini bajarish uchun foydalaniladi. Buning uchun bajarilishi talab qilingan kodlar orasiga 'or' operatorini qo'yish kerak."
        for text in result['matches']:
            if text == 'boolean':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}(mantiqiy)'\tqiymatlar taqqoslash operatorlari yordamida turli ifodalarni solishtirishda True yoki False qiymat qaaytaradi."
        for text in result['matches']:
            if text == 'in':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin."
        for text in result['matches']:
            if text == 'not in':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori yordamida biz ro'yxatning tarkibida ma'lum bir element yo'qligini tekshirishimiz mumkin."
        for text in result['matches']:
            if text == 'dictionary':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}(lug'at)'\tbir obyektga bog'liq ma'lumotlarni kalit so'z va qiymat juftligi ko'rinishida saqlash imkonini beradi."
        for text in result['matches']:
            if text == 'set':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}(to'plam)'\tPythonda yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni saqlashda qo'llaniladi."
        for text in result['matches']:
            if text == 'get':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tmetodi yordamida lug'atga murojaat etish va mavjud bo'lmagan kalitning o'rniga biror xabar qaytarishimiz mumkin."
        for text in result['matches']:
            if text == 'items':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini olishimiz mumkin."
        for text in result['matches']:
            if text == 'keys':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida lug'at ichidagi barcha kalit so'zlarni olishimiz mumkin."
        for text in result['matches']:
            if text == 'values':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida lug'at ichidagi barcha qiymatlarni olishimiz mumkin."
        for text in result['matches']:
            if text == 'discard':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida to'plam ichidagi elementlarni o'chirishimiz mumkin."
        for text in result['matches']:
            if text == 'add':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida to'plamga bitta element qo'shishimiz mumkin."
        for text in result['matches']:
            if text == 'update':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida to'plamga bir nechta element qo'shishimiz mumkin."
        for text in result['matches']:
            if text == 'intersection':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tPythondagi mantiqiy qiymatlardan biri bo'lib, berilgan shart bajarilmaganligini ifodalaydi."
        for text in result['matches']:
            if text == 'difference':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida birinchi to'plamda bor, ammo ikkinchi to'plamda mavjud bo'lmagan elementlarni olishimiz mumkin. Uning o'rniga - operatoridan ham foydalana olamiz."
        for text in result['matches']:
            if text == 'symmetric_difference':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida ikki to'plamdagi bir xil bo'lmagan elementlarni olishimiz mumkin. Uning o'rniga ^ operatoridan ham foydalana olamiz."
        for text in result['matches']:
            if text == 'while loop':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tbiror bir shartga bog'langan bo'ladi. Ya'ni uning badanidagi kodning takrorlanishi, toki biror shart bajarilguniga qadar davom etadi."
        for text in result['matches']:
            if text == 'break':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori loop(sikl) bajarilishini loop badanidan to'xtatish imkonini beradi."
        for text in result['matches']:
            if text == 'continue':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori biror shart bajarilganda, aynan shuni tashlab ketish uchun foydalaniladi."
        for text in result['matches']:
            if text == 'infinite loop':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}(abadiy sikl)'\tturli mantiqiy xatalor asosida yuzaga kelib, uni to'xtatmagunimizcha davom etadi. Uni to'xtatish uchun Ctrl+C tugmalarini bosish kerak."
        for text in result['matches']:
            if text == 'try-except':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori xatolik mavjud bo'lsa uni oldini olishda foydalaniladi. Ya'ni try operatori badanida bajarilishi kerak bo'lgan kod yoziladi, except operatori badanida esa, xatolik yuz berganda bajarilishi kerak bo'lgan kod yoziladi."
        for text in result['matches']:
            if text == 'function':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}(funksiya)'\tma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisidir. Funksiyalar, odatda, ma'lumotlarni qayta ishlaydi va biror natija qaytaradi."
        for text in result['matches']:
            if text == 'def':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori yordamida Pythonga funksiya yaratayotganimizni bildiramiz va undan so'ng funksiyaga nom beramiz."
        for text in result['matches']:
            if text == 'doc-string':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfunksiyaning qanday ishlashi haqida kiritilgan qisqacha ma'lumot hisoblanadi. U funksiya badanining ilk qatorida uchta qo'shtirnoq ichida yoziladi."
        for text in result['matches']:
            if text == 'argument':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tfoydalanuvchi funksiyaga murojaat etishda funksiyaga uzatgan qiymat hisoblanadi."
        for text in result['matches']:
            if text == 'parameter':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tfunksiya yaratishda qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat hisoblanadi."
        for text in result['matches']:
            if text == '*args':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfunksiya qabul qiladigan parametrlar soni noaniq bo'lsa, funksiya yaratishda foydalaniladi(*args)."
        for text in result['matches']:
            if text == '*kwargs':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfunksiya qabul qiladigan kalit-qiymat ko'rinishidagi parametrlar soni noaniq bo'lsa, funksiya yaratishda foydalaniladi(**kwargs)."
        for text in result['matches']:
            if text == 'from-import':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tmodul ichidagi muayyan funksiyaga murojaat etishda foydalaniladi."
        for text in result['matches']:
            if text == 'module':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tloyihamiz ichidagi alohida fayl bo'lib, dastur davomida ishlatiladigan funksiyalarni mana shu faylga joylab qo'yishimiz mumkin."
        for text in result['matches']:
            if text == 'math':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tmatematik hisob-kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan modul."
        for text in result['matches']:
            if text == 'sqrt':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tqavs ichida berilgan qiymatlarning kvadrat ildizini qaytaradi."
        for text in result['matches']:
            if text == 'pow':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tx ning n-darajasini qaytaruvchi funksiya."
        for text in result['matches']:
            if text == 'pi':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tп ning qiymatini saqlovchi o'zgaruvchi."
        for text in result['matches']:
            if text == 'log2':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tx ning 2 lik logarifmini qaytaruvchi funksiya."
        for text in result['matches']:
            if text == 'log10':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tx ning 10 lik logarifmini qaytaruvchi funksiya."
        for text in result['matches']:
            if text == 'random':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tasosan tasodifiy sonlar bilan ishlovchi funksiyalarga boy modul."
        for text in result['matches']:
            if text == 'randint':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}(a,b)'\tfunksiyasi a va b son oralig'idagi tasodifiy butun sonni qaytaradi."
        for text in result['matches']:
            if text == 'choice':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}(x)'\tfunksiyasi berilgan x argumentning ichidagi tasodifiy elementni qaytaradi."
        for text in result['matches']:
            if text == 'shuffle':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}(x)'\tfunksiyasi x ichidagi elementlarni tasodifiy tartibda qaytaradi."
        for text in result['matches']:
            if text == 'sample':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}(x,k)'\tx ro'yxat ichidagi tasodifiy k ta elementni qaytaruvchi funksiya."
        for text in result['matches']:
            if text == 'lambda':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tnomsiz, vaqtinchalik funksiyalar yaratish imkonini beruvchi Pythinning o'ziga xos xususiyatlaridan biri. (lambda argument: ifoda)"
        for text in result['matches']:
            if text == 'map':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi argument sifatida ro'yxat va boshqa bir funksiya qabul qilib, ro'yxat elementlariga qabul qilingan funksiya yordamida ishlov beradi."
        for text in result['matches']:
            if text == 'filter':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi argument sifatida ro'yxat va boshqa bir funksiya qabul qilib, ro'yxat elementlarini berilgan funksiya yordamida saralaydi."
        for text in result['matches']:
            if text == 'class':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tobyekt yaratish uchun shablon yoki qolip."
        for text in result['matches']:
            if text == 'pass':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\toperatori bo'sh metod yaratishda foydalaniladi."
        for text in result['matches']:
            if text == 'dir':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}()'\tfunksiyasi yordamida istalgan obyekt yoki klassning metodlarini ko'rib olishimiz mumkin."
        for text in result['matches']:
            if text == '__dict__':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}'\tmetodi obyektning xususiyatlarini lug'at ko'rinishida qaytaradi."
        for text in result['matches']:
            if text == 'dunder':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tobyektlar bilan ishlaydigan metodlarning ikki pastki chiziq bilan yozilishidir."
        for text in result['matches']:
            if text == 'object':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tOOP da o'zaro bog'liq bo'lgan o'zgaruvchilar va funksiyalar bitta konteynerga jamlanadi, bular obyekt deb ataladi."
        for text in result['matches']:
            if text == 'method':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'.\tHar bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bular shu klassga tegishli metodlar hisoblanadi."
        for text in result['matches']:
            if text == 'read':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi yordamida fayl obyektining tarkibidagi kerakli matnga murojaat qilishimiz mumkin."
        for text in result['matches']:
            if text == 'open':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tfunksiyasi yordamida biror faylni ochishimiz mumkin. U faylni obyekt sifatida qaytaradi."
        for text in result['matches']:
            if text == 'close':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tfunksiyasi yordamida biror bir faylni yopishimiz mumkin."
        for text in result['matches']:
            if text == 'replace':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodi matn tarkibidagi biror harf yoki belgini boshqa harf yoki belgi bilan almashtirish uchun ishlatiladi."
        for text in result['matches']:
            if text == 'readlines':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodidan biror fayldagi qatorlarni ro'yxat ko'rinishida saqlab olish uchun foydalanamiz."
        for text in result['matches']:
            if text == 'w':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylni yozish uchun ochishda foydalaniladi. open('file.txt', 'w')"
        for text in result['matches']:
            if text == 'r':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylni o'qish uchun ochishda foydalaniladi. open('file.txt', 'r')"
        for text in result['matches']:
            if text == 'w+':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylni o'qish va yozish uchun ochishda foydalaniladi. open('file.txt', 'w+')"
        for text in result['matches']:
            if text == 'r+':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylni o'qish va yozish uchun ochishda foydalaniladi. open('file.txt', 'r+')"
        for text in result['matches']:
            if text == 'a':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylga ma'lumot qo'shish uchun ochishda foydalaniladi. open('file.txt', 'a')"
        for text in result['matches']:
            if text == 'a+':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text}'\tfaylga ma'lumot qo'shish va o'qish uchun ochishda foydalaniladi. open('file.txt', 'a+')"
        for text in result['matches']:
            if text == 'write':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'.{text}()'\tmetodidan ochilgan faylga ma'lumot qo'shishda foydalanamiz."
        for text in result['matches']:
            if text == 'none':
                response = f"❌\t{function}\t(Bunday ma'lumot topilmadi)\n"
                response += f"➡\t'{text.capitalize()}'\tPythonda kalit so'z bo'lib, qiymat mavjud emasligini bildiradi."
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



























































































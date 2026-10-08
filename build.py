"""Builds the BoBudget site: one template, three languages.

    python build.py

Writes index.html (English), ru/index.html, uk/index.html, 404.html,
sitemap.xml and robots.txt. Images live in assets/img (app screens are taken
from the store screenshots of the app repo).
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://bogdanhere1.github.io/bobudget/"
API = "https://budget-api-production-ce25.up.railway.app"
BOT = "https://t.me/bobudget_bot"
LANGS = ["en", "ru", "uk"]
PATH = {"en": "", "ru": "ru/", "uk": "uk/"}
NAMES = {"en": "EN", "ru": "RU", "uk": "UA"}

T = {
    "ru": {
        "title": "BoBudget — учёт расходов голосом, текстом и по фото чека",
        "desc": "BoBudget — личный учёт расходов: скажите «кофе 5 и такси 12», и траты сами разложатся по категориям. Лимит на день, календарь трат, аналитика и кот, которого кормят ваши записи.",
        "eyebrow": "Скоро в Google Play и App Store",
        "h1": 'Учёт расходов, <span class="mark">в который хочется</span> записывать траты',
        "lead": "Голосом, текстом или по фото чека — BoBudget сам разберёт суммы и разложит траты по категориям. А ваш кот следит, чтобы вы не забывали.",
        "soon": "скоро",
        "tg": "Попробовать в Telegram",
        "fast_h": "Запись за секунды",
        "fast_sub": "Самое скучное в учёте расходов — записывать. Поэтому в BoBudget это занимает пару секунд.",
        "fast": [
            ("🎙", "Голосом", "«Кофе 5 лари и такси 12» — одна фраза, две траты, суммы и категории расставлены."),
            ("⌨️", "Текстом", "Напишите как удобно, хоть несколько трат сразу — BoBudget поймёт."),
            ("🧾", "По фото чека", "Сфотографируйте чек — позиции распознаются автоматически.", "Pro"),
        ],
        "screens_h": "Как это выглядит",
        "screens": ["Весь бюджет на одном экране", "Куда уходят деньги", "Календарь трат", "Питомец", "Комната кота", "Новая трата"],
        "budget_h": "Понятный бюджет",
        "budget_sub": "Не таблица ради таблицы, а ответ на вопрос «сколько я могу потратить сегодня».",
        "budget": [
            ("📅", "Лимит на день", "План на месяц превращается в сумму, которую спокойно можно потратить сегодня."),
            ("🗓", "Календарь трат", "Сразу видно, какие дни были дорогими и почему."),
            ("📊", "Аналитика", "Категории с цветами, которые вы выбираете сами, и динамика по месяцам."),
            ("🔁", "Регулярные платежи", "Подписки, аренда, связь — напоминания и учёт без ручного ввода."),
            ("🐷", "Копилки", "Цели с прогрессом: отпуск, техника, подушка безопасности."),
            ("💱", "43 валюты", "Трата в любой валюте пересчитывается по официальному курсу на её дату."),
        ],
        "pet_h": "Питомец, который мотивирует",
        "pet_p": "Каждая записанная трата кормит вашего кота. Он растёт вместе с вашей привычкой вести бюджет.",
        "pet": [
            "<b>Опыт и уровни</b> — за каждую запись",
            "<b>Серии дней</b> — не пропускайте, и кот будет счастлив",
            "<b>Лапки</b> — валюта для покупок: лежанка, когтеточка, игрушки",
            "<b>Комната кота</b> — обставьте её по своему вкусу",
        ],
        "sec_h": "Ваши данные — только ваши",
        "sec_p": "Финансы — личное. BoBudget не показывает рекламу и не продаёт данные.",
        "sec": [
            "<b>PIN-код и биометрия</b> — вход по отпечатку пальца или Face ID",
            "<b>Шифрование AES-256</b> — заметки, тексты голосовых, имя и email шифруются до записи на сервер",
            "<b>Без рекламы и трекеров</b> — данные не передаются рекламным сетям",
            "<b>Удаление в один шаг</b> — аккаунт и все данные можно удалить в любой момент",
        ],
        "pro_h": "BoBudget Pro",
        "pro_p": "Основные функции бесплатны. Pro — для тех, кто хочет больше:",
        "pro": ["Голосовой ввод без ограничений", "Распознавание фото чеков", "AI-разбор трат и советы раз в месяц"],
        "pro_note": "Подписка оформляется внутри приложения через Google Play или App Store и отменяется в любой момент.",
        "faq_h": "Вопросы",
        "faq": [
            ("Сколько это стоит?", "Приложение бесплатное. Дополнительные возможности — в подписке BoBudget Pro."),
            ("Где хранятся мои данные?", "На защищённом сервере в Европе. Личные поля шифруются, все соединения идут по HTTPS. Подробно — в политике конфиденциальности."),
            ("Как удалить аккаунт?", "В приложении: Личный кабинет → Удалить аккаунт. Или без приложения — на странице удаления аккаунта."),
            ("Когда приложение появится в магазинах?", "Сейчас идёт тестирование. BoBudget уже работает в Telegram — можно попробовать там."),
            ("Это финансовая консультация?", "Нет. BoBudget — инструмент учёта: решения вы принимаете сами."),
        ],
        "privacy": "Конфиденциальность", "terms": "Условия", "delete": "Удаление аккаунта", "telegram": "Telegram",
        "foot": "BoBudget — инструмент учёта расходов, а не финансовая консультация.",
    },
    "en": {
        "title": "BoBudget — expense tracker by voice, text and receipt photo",
        "desc": "BoBudget is a personal expense tracker: say “coffee 5 and a taxi 12” and it sorts the spending into categories. A daily limit, a spending calendar, insights and a cat that your entries keep fed.",
        "eyebrow": "Coming soon to Google Play and the App Store",
        "h1": 'An expense tracker <span class="mark">you’ll actually</span> want to use',
        "lead": "By voice, text or receipt photo — BoBudget works out the amounts and sorts your spending into categories. And your cat makes sure you don’t forget.",
        "soon": "coming soon",
        "tg": "Try it in Telegram",
        "fast_h": "Log it in seconds",
        "fast_sub": "The boring part of budgeting is writing things down. In BoBudget it takes a couple of seconds.",
        "fast": [
            ("🎙", "By voice", "“Coffee 5 and a taxi 12” — one sentence, two expenses, amounts and categories filled in."),
            ("⌨️", "By text", "Type it any way you like, several expenses at once — BoBudget gets it."),
            ("🧾", "By receipt photo", "Snap the receipt — line items are recognized automatically.", "Pro"),
        ],
        "screens_h": "What it looks like",
        "screens": ["Your whole budget at a glance", "Where the money goes", "Spending calendar", "Your pet", "The cat’s room", "New expense"],
        "budget_h": "A budget that makes sense",
        "budget_sub": "Not a spreadsheet for its own sake, but an answer to “how much can I spend today?”",
        "budget": [
            ("📅", "Daily limit", "Your monthly plan becomes an amount you can comfortably spend today."),
            ("🗓", "Spending calendar", "See at a glance which days cost the most, and why."),
            ("📊", "Insights", "Categories in colors you choose, and month-by-month trends."),
            ("🔁", "Recurring payments", "Subscriptions, rent, phone — reminders and tracking without typing."),
            ("🐷", "Savings goals", "Goals with progress: a holiday, new gear, an emergency fund."),
            ("💱", "43 currencies", "Foreign spending is converted at the official rate for its date."),
        ],
        "pet_h": "A pet that keeps you going",
        "pet_p": "Every expense you log feeds your cat. It grows along with your budgeting habit.",
        "pet": [
            "<b>XP and levels</b> — for every entry",
            "<b>Streaks</b> — don’t miss a day and your cat stays happy",
            "<b>Paws</b> — spend them on a bed, a scratcher, toys",
            "<b>The cat’s room</b> — furnish it your way",
        ],
        "sec_h": "Your data stays yours",
        "sec_p": "Money is personal. BoBudget shows no ads and never sells your data.",
        "sec": [
            "<b>PIN and biometrics</b> — unlock with your fingerprint or Face ID",
            "<b>AES-256 encryption</b> — notes, voice texts, your name and email are encrypted before they reach the server",
            "<b>No ads, no trackers</b> — nothing is shared with ad networks",
            "<b>One-step deletion</b> — delete your account and all data at any time",
        ],
        "pro_h": "BoBudget Pro",
        "pro_p": "The core features are free. Pro is for those who want more:",
        "pro": ["Unlimited voice entry", "Receipt photo recognition", "A monthly AI review of your spending with tips"],
        "pro_note": "The subscription is purchased inside the app through Google Play or the App Store and can be cancelled anytime.",
        "faq_h": "Questions",
        "faq": [
            ("How much does it cost?", "The app is free. Extra features come with the BoBudget Pro subscription."),
            ("Where is my data stored?", "On a secured server in Europe. Personal fields are encrypted and every connection uses HTTPS. See the privacy policy for details."),
            ("How do I delete my account?", "In the app: Account → Delete account. Or without the app, on the account deletion page."),
            ("When will it be in the stores?", "Testing is under way. BoBudget already works in Telegram — you can try it there."),
            ("Is this financial advice?", "No. BoBudget is a tracking tool; the decisions are yours."),
        ],
        "privacy": "Privacy", "terms": "Terms", "delete": "Delete account", "telegram": "Telegram",
        "foot": "BoBudget is an expense tracking tool, not financial advice.",
    },
    "uk": {
        "title": "BoBudget — облік витрат голосом, текстом і за фото чека",
        "desc": "BoBudget — особистий облік витрат: скажіть «кава 5 і таксі 12», і витрати самі розкладуться за категоріями. Ліміт на день, календар витрат, аналітика і кіт, якого годують ваші записи.",
        "eyebrow": "Незабаром у Google Play і App Store",
        "h1": 'Облік витрат, <span class="mark">у який хочеться</span> записувати витрати',
        "lead": "Голосом, текстом або за фото чека — BoBudget сам розбере суми й розкладе витрати за категоріями. А ваш кіт стежить, щоб ви не забували.",
        "soon": "незабаром",
        "tg": "Спробувати в Telegram",
        "fast_h": "Запис за секунди",
        "fast_sub": "Найнудніше в обліку витрат — записувати. Тому в BoBudget це займає пару секунд.",
        "fast": [
            ("🎙", "Голосом", "«Кава 5 ларі і таксі 12» — одна фраза, дві витрати, суми й категорії розставлені."),
            ("⌨️", "Текстом", "Напишіть як зручно, хоч кілька витрат одразу — BoBudget зрозуміє."),
            ("🧾", "За фото чека", "Сфотографуйте чек — позиції розпізнаються автоматично.", "Pro"),
        ],
        "screens_h": "Як це виглядає",
        "screens": ["Весь бюджет на одному екрані", "Куди йдуть гроші", "Календар витрат", "Улюбленець", "Кімната кота", "Нова витрата"],
        "budget_h": "Зрозумілий бюджет",
        "budget_sub": "Не таблиця заради таблиці, а відповідь на питання «скільки я можу витратити сьогодні».",
        "budget": [
            ("📅", "Ліміт на день", "План на місяць перетворюється на суму, яку спокійно можна витратити сьогодні."),
            ("🗓", "Календар витрат", "Одразу видно, які дні були дорогими і чому."),
            ("📊", "Аналітика", "Категорії з кольорами, які ви обираєте самі, і динаміка за місяцями."),
            ("🔁", "Регулярні платежі", "Підписки, оренда, зв’язок — нагадування та облік без ручного введення."),
            ("🐷", "Скарбнички", "Цілі з прогресом: відпустка, техніка, фінансова подушка."),
            ("💱", "43 валюти", "Витрата в будь-якій валюті перераховується за офіційним курсом на її дату."),
        ],
        "pet_h": "Улюбленець, який мотивує",
        "pet_p": "Кожна записана витрата годує вашого кота. Він росте разом із вашою звичкою вести бюджет.",
        "pet": [
            "<b>Досвід і рівні</b> — за кожен запис",
            "<b>Серії днів</b> — не пропускайте, і кіт буде щасливий",
            "<b>Лапки</b> — валюта для покупок: лежанка, дряпка, іграшки",
            "<b>Кімната кота</b> — облаштуйте її на свій смак",
        ],
        "sec_h": "Ваші дані — лише ваші",
        "sec_p": "Фінанси — це особисте. BoBudget не показує рекламу і не продає дані.",
        "sec": [
            "<b>PIN-код і біометрія</b> — вхід за відбитком пальця або Face ID",
            "<b>Шифрування AES-256</b> — нотатки, тексти голосових, ім’я та email шифруються до запису на сервер",
            "<b>Без реклами й трекерів</b> — дані не передаються рекламним мережам",
            "<b>Видалення в один крок</b> — акаунт і всі дані можна видалити будь-коли",
        ],
        "pro_h": "BoBudget Pro",
        "pro_p": "Основні функції безкоштовні. Pro — для тих, хто хоче більше:",
        "pro": ["Голосове введення без обмежень", "Розпізнавання фото чеків", "AI-аналіз витрат і поради раз на місяць"],
        "pro_note": "Підписка оформлюється в застосунку через Google Play або App Store і скасовується будь-коли.",
        "faq_h": "Питання",
        "faq": [
            ("Скільки це коштує?", "Застосунок безкоштовний. Додаткові можливості — у підписці BoBudget Pro."),
            ("Де зберігаються мої дані?", "На захищеному сервері в Європі. Особисті поля шифруються, усі з’єднання йдуть через HTTPS. Докладно — у політиці конфіденційності."),
            ("Як видалити акаунт?", "У застосунку: Особистий кабінет → Видалити акаунт. Або без застосунку — на сторінці видалення акаунта."),
            ("Коли застосунок з’явиться в магазинах?", "Зараз триває тестування. BoBudget уже працює в Telegram — можна спробувати там."),
            ("Це фінансова консультація?", "Ні. BoBudget — інструмент обліку: рішення ви ухвалюєте самі."),
        ],
        "privacy": "Конфіденційність", "terms": "Умови", "delete": "Видалення акаунта", "telegram": "Telegram",
        "foot": "BoBudget — інструмент обліку витрат, а не фінансова консультація.",
    },
}

SCREEN_IDS = ["01-home", "02-analytics", "03-calendar", "04-pet", "05-room", "06-add"]

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>'


def page(lang: str) -> str:
    t = T[lang]
    pre = "../" if PATH[lang] else ""
    img = f"{pre}assets/img"
    url = BASE + PATH[lang]
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE + PATH[l]}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    langs = "".join(
        f'<a href="{pre}{PATH[l]}" hreflang="{l}" data-lang="{l}"'
        f'{" aria-current=" + chr(34) + "true" + chr(34) if l == lang else ""}>{NAMES[l]}</a>'
        for l in LANGS
    )
    fast = "".join(
        f'<div class="card"><div class="ic">{ic}</div><h3>{escape(h)}</h3><p>{escape(p)}</p>'
        + (f'<span class="tag">{rest[0]}</span>' if rest else "")
        + "</div>"
        for ic, h, p, *rest in t["fast"]
    )
    budget = "".join(
        f'<div class="card"><div class="ic">{ic}</div><h3>{escape(h)}</h3><p>{escape(p)}</p></div>'
        for ic, h, p in t["budget"]
    )
    screens = "".join(
        f'<figure><div class="shot"><img src="{img}/{lang}-{sid}.webp" width="720" height="1520" '
        f'loading="lazy" alt="{escape(cap)}"></div><figcaption>{escape(cap)}</figcaption></figure>'
        for sid, cap in zip(SCREEN_IDS, t["screens"])
    )
    ticks = lambda items: "".join(f"<li><span>{i}</span></li>" for i in items)  # noqa: E731
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in t["faq"])
    pro = "".join(f"<li>{escape(x)}</li>" for x in t["pro"])
    store = lambda name: (  # noqa: E731
        f'<div class="store">{ICON_PHONE}<span><b>{name}</b><small>{escape(t["soon"])}</small></span></div>'
    )
    redirect = ""
    if lang == "en":
        # first visit to the root: follow the browser language (ru/uk); a choice made with the switcher sticks
        redirect = """<script>
try{var s=localStorage.getItem('lang');var n=(navigator.language||'').slice(0,2).toLowerCase();
var to=s||(n==='ru'||n==='uk'||n==='be'?(n==='uk'?'uk':'ru'):'');if(to&&to!=='en')location.replace(to+'/');}catch(e){}
</script>"""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t["title"])}</title>
<meta name="description" content="{escape(t["desc"])}">
<link rel="canonical" href="{url}">
{alts}
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(t["title"])}">
<meta property="og:description" content="{escape(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/img/og-{lang}.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#e6e8f0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#272934" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" href="{img}/favicon.png">
<link rel="apple-touch-icon" href="{img}/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css">
{redirect}
</head>
<body>
<header class="top"><div class="wrap">
  <a href="{pre}{PATH[lang]}" aria-label="BoBudget"><img class="logo-light" src="{img}/logo-light.png" alt="BoBudget" width="424" height="110"><img class="logo-dark" src="{img}/logo-dark.png" alt="BoBudget" width="424" height="110"></a>
  <nav class="langs" aria-label="Language">{langs}</nav>
</div></header>

<main>
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">{escape(t["eyebrow"])}</span>
    <h1>{t["h1"]}</h1>
    <p class="lead">{escape(t["lead"])}</p>
    <div class="stores">{store("Google Play")}{store("App Store")}<a class="tg" href="{BOT}" rel="noopener">{escape(t["tg"])}</a></div>
  </div>
  <div class="phone-stage"><div class="glow"></div><div class="phone"><img src="{img}/{lang}-01-home.webp" width="720" height="1520" alt="{escape(t["screens"][0])}" fetchpriority="high"></div></div>
</div></section>

<section><div class="wrap">
  <h2>{escape(t["fast_h"])}</h2><p class="sub">{escape(t["fast_sub"])}</p>
  <div class="grid3">{fast}</div>
</div></section>

<section><div class="wrap">
  <h2>{escape(t["screens_h"])}</h2>
  <div class="screens">{screens}</div>
</div></section>

<section><div class="wrap">
  <h2>{escape(t["budget_h"])}</h2><p class="sub">{escape(t["budget_sub"])}</p>
  <div class="grid3">{budget}</div>
</div></section>

<section><div class="wrap split">
  <div class="phone-col"><div class="phone"><img src="{img}/{lang}-04-pet.webp" width="720" height="1520" loading="lazy" alt="{escape(t["screens"][3])}"></div></div>
  <div><h2>{escape(t["pet_h"])}</h2><p class="sub">{escape(t["pet_p"])}</p><ul class="ticks">{ticks(t["pet"])}</ul></div>
</div></section>

<section><div class="wrap split rev">
  <div><h2>{escape(t["sec_h"])}</h2><p class="sub">{escape(t["sec_p"])}</p><ul class="ticks">{ticks(t["sec"])}</ul></div>
  <div class="phone-col"><div class="phone"><img src="{img}/{lang}-02-analytics.webp" width="720" height="1520" loading="lazy" alt="{escape(t["screens"][1])}"></div></div>
</div></section>

<section><div class="wrap">
  <div class="pro"><h2>{escape(t["pro_h"])}</h2><p>{escape(t["pro_p"])}</p><ul>{pro}</ul><p style="margin:16px 0 0">{escape(t["pro_note"])}</p></div>
</div></section>

<section><div class="wrap">
  <h2>{escape(t["faq_h"])}</h2>
  {faq}
</div></section>
</main>

<footer><div class="wrap">
  <div class="note"><img class="logo-light" src="{img}/logo-light.png" alt="BoBudget" width="140" height="36" style="height:26px;width:auto;margin-bottom:10px"><img class="logo-dark" src="{img}/logo-dark.png" alt="" width="140" height="36" style="height:26px;width:auto;margin-bottom:10px">
  <div>{escape(t["foot"])}</div><div>© 2026 BoBudget</div></div>
  <nav><a href="{API}/privacy/">{escape(t["privacy"])}</a><a href="{API}/terms/">{escape(t["terms"])}</a><a href="{API}/delete-account/">{escape(t["delete"])}</a><a href="{BOT}" rel="noopener">{escape(t["telegram"])}</a></nav>
</div></footer>
<script>
document.querySelectorAll('.langs a').forEach(function(a){{a.addEventListener('click',function(){{try{{localStorage.setItem('lang',a.dataset.lang)}}catch(e){{}}}})}});
</script>
</body>
</html>
"""


NOT_FOUND = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>BoBudget</title><link rel="stylesheet" href="/bobudget/assets/site.css"></head>
<body><main class="wrap" style="padding:80px 20px;text-align:center">
<h1 style="font-size:40px">404</h1><p class="sub" style="margin:0 auto 24px">Page not found · Страница не найдена</p>
<a class="tg" href="/bobudget/">BoBudget</a></main></body></html>
"""


def main() -> None:
    for lang in LANGS:
        out = ROOT / PATH[lang] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
    (ROOT / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    urls = "".join(f"<url><loc>{BASE + PATH[l]}</loc></url>" for l in LANGS)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("site built:", ", ".join(BASE + PATH[l] for l in LANGS))


if __name__ == "__main__":
    main()

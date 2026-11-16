# بوت حجز طاولة مطعم - ثناء | thanaa.codes

print("=" * 40)
print("🍽️ مطعم ثناء - اهلا فيك")
print("=" * 40)

print("\n✨ انواع الطاولات:")
print("1. طاولة لشخصين - 50 ريال")
print("2. طاولة لـ 4 اشخاص - 80 ريال")
print("3. طاولة لـ 6 اشخاص - 120 ريال")
print("4. طاولة VIP - 200 ريال")

choice = input("\nاختاري رقم الطاولة: ")

tables = {
    "1": ("طاولة لشخصين", 50),
    "2": ("طاولة لـ 4 اشخاص", 80),
    "3": ("طاولة لـ 6 اشخاص", 120),
    "4": ("طاولة VIP", 200),
}

table_name, table_price = tables.get(choice, ("غير معروفة", 0))
print(f"\nاخترتي: {table_name} - {table_price} ريال")

print("\n🗓️ الايام:")
print("1. السبت")
print("2. الاحد")
print("3. الاثنين")
print("4. الثلاثاء")
print("5. الاربعاء")
print("6. الخميس")
print("7. الجمعة")

day = input("اختاري اليوم: ")
days = {"1":"السبت","2":"الاحد","3":"الاثنين","4":"الثلاثاء","5":"الاربعاء","6":"الخميس","7":"الجمعة"}
day_name = days.get(day, "غير محدد")

print("\n⏰ الاوقات:")
print("1. 12 ظهرا")
print("2. 2 عصرا")
print("3. 4 عصرا")
print("4. 6 مساء")
print("5. 8 مساء")
print("6. 10 مساء")

time_choice = input("اختاري الوقت: ")
times = {"1":"12 ظهرا","2":"2 عصرا","3":"4 عصرا","4":"6 مساء","5":"8 مساء","6":"10 مساء"}
time_name = times.get(time_choice, "غير محدد")

print("\n--- بيانات الحجز ---")
name = input("اسمك: ")
phone = input("رقم جوالك: ")
persons = input("كم عدد الاشخاص؟ ")

print("\n" + "=" * 40)
print("✅ تم تأكيد حجزك!")
print("=" * 40)
print(f"الاسم: {name}")
print(f"الجوال: {phone}")
print(f"الطاولة: {table_name}")
print(f"عدد الاشخاص: {persons}")
print(f"اليوم: {day_name}")
print(f"الوقت: {time_name}")
print(f"السعر: {table_price} ريال")
print("\nننتظرك في مطعم ثناء 💖")
print("=" * 40)

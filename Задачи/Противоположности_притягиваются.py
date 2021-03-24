# Тимми и Сара думают, что они влюблены, но о том, где они живут, они узнают только после того, как сорвут по цветку.
# Если один из цветов имеет четное число лепестков, а другой-нечетное, это означает, что они влюблены.
# Напишите функцию, которая будет принимать количество лепестков каждого цветка и возвращать true, если они влюблены, и false, если нет.

def lovefunc(flower1, flower2):
    if flower1 % 2 == 0:
        if flower2 % 2 == 0:
            return False
        else:
            return True
    else:
        if flower1 % 2 > 0:
            if flower2 % 2 > 0:
                return False
            else:
                return True

print(lovefunc(1,3))
print(lovefunc(34,1))
print(lovefunc(11,8))
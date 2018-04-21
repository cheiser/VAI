import re
from PIL import Image

# THIS DOES NOT WORK!

def subimg_location(haystack, needle):
    haystack = haystack.convert('RGB')
    needle   = needle.convert('RGB')

    haystack_str = haystack.tostring()
    needle_str   = needle.tostring()

    gap_size = (haystack.size[0] - needle.size[0]) * 3
    gap_regex = '.{' + str(gap_size) + '}'

    # Split b into needle.size[0] chunks
    chunk_size = needle.size[0] * 3
    split = [needle_str[i:i+chunk_size] for i in range(0, len(needle_str), chunk_size)]

    # Build regex
    regex = re.escape(split[0])
    for i in xrange(1, len(split)):
        regex += gap_regex + re.escape(split[i])

    p = re.compile(regex)
    m = p.search(haystack_str)

    if not m:
        return None

    x, _ = m.span()

    left = x % (haystack.size[0] * 3) / 3
    top  = x / haystack.size[0] / 3

    return (left, top)

def main():
    super = Image.open("screenshots/super.PNG")
    sub = Image.open("screenshots/sub.PNG")

    (left, top) = subimg_location(super, sub)

    print left.tobytes()
    #print("left: " + str(left) + "\ntop: " + str(top))


if __name__ == '__main__':
    main()
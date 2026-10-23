wrapping_paper_sa = 0
ribbon_size = 0

with open('inputs/2.txt', 'r') as presents:
    for present in presents:
        ls, ws, hs = present.split("x")
        l, w, h = int(ls), int(ws), int(hs)
        dimensions = [l, w, h]
        dimensions.sort()

        side_a = l*w
        side_b = w*h
        side_c = l*h

        slack = dimensions[0]*dimensions[1]

        wrapping_paper_sa += 2*side_a + 2*side_b + 2* side_c + slack

        ribon_wrap = 2*dimensions[0] + 2*dimensions[1]
        ribbon_bow = l*w*h

        ribbon_size += ribon_wrap + ribbon_bow

print("Elves should order " + str(wrapping_paper_sa) + " square feet of wrapping paper.")
print("Elves need " + str(ribbon_size) + " feet of ribbon.")


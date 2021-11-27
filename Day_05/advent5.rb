file = File.open("puzzle.txt")
file_data = file.readlines.map(&:chomp)

ids = Array.new

file_data.each do | i |
    x = 0
    y = 127
    z = 64
    a = 0
    b = 7
    c = 4
    instructions = i.split("")
    for j in instructions
        if j == "F"
            y -= z
            z /= 2
        elsif j == "B"
            x += z
            z /= 2
        elsif j == "R"
            a += c
            c /= 2
        else
            b -= c
            c /= 2
        end
    end
ids << (x * 8 + a)
end
puts "Solution for part 1 is:", ids.max

ids_range =* (ids.min..ids.max)
puts "Solution for part 2 is:", ids_range.sum - ids.sum
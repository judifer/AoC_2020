file = File.open("day1_2020.txt")
file_data = file.readlines.map(&:to_i)

def part_one(f)
    for i in f
        a = 2020 - i
        if f.include?(a)
            puts a * i
            break
        end
    end
end

def part_two(f)
    for i in f
        for j in f
            s = 2020 - i - j
            if f.include?(s)
                puts i * j * s
                break
            end
        end
    end
end

puts "The solution for part one is:"
part_one(file_data)
puts "The solution for part two is:"
part_two(file_data)
t = gets.chomp.to_i




t.times do
  n = gets.chomp.to_i
  a = gets.chomp.split.map(&:to_i)

  a.sort!

  median = 0
  operations = 0
  x = 0

  if n % 2 == 0
    operations = a[n / 2 - 1]
    x = n / 2 - 1
  else
    operations = a[n / 2]
    x = n / 2
  end

  (x...n).each do |i|
    if a[i] == operations
      median += 1
    end
  end

  puts median
end

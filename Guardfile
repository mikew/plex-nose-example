def python_unittest(test_file)
  return unless File.exist? test_file

  runner = case RUBY_PLATFORM
  when /linux/  then 'ubuntu'
  when /darwin/ then 'osx'
  end

  system *[ "./run-#{runner}.sh", test_file ]
end

def sanitize!(env)
  env.to_s.
    gsub(/\r?\n/, ' ').
    gsub(/\t/, ' ').
    gsub(/ +/, ' ').
    gsub('~/', ENV['HOME'] + '/')
end

guard 'shell' do
  watch(%r{Contents/Code/(.*).py$})       {|m| python_unittest "Contents/Tests/test_#{m[1]}.py" }
  watch(%r{Contents/Tests/test_(.*).py$}) {|m| python_unittest "Contents/Tests/test_#{m[1]}.py" }
end

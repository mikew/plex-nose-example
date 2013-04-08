#os.path.expanduser('~/Library/Application Support/Plex Media Server/Plug-ins/Framework.bundle/Contents/Resources/Versions/2/Python')
def env_for_osx
  framework_resources = '~/Library/Application Support/Plex Media Server/Plug-ins/Framework.bundle/Contents/Resources'
  dyld_path = [
    "#{framework_resources}/Platforms/MacOSX/i386/Frameworks/",
    "#{framework_resources}/Versions/2/Platforms/MacOSX/i386/Frameworks/",
    "#{framework_resources}/Versions/2/Frameworks/"
  ].join ':'

  <<ENV
  DYLD_LIBRARY_PATH="#{dyld_path}"
  PLEX_FRAMEWORK_PATH="#{framework_resources}/Versions/2/Python"
ENV
end

def env_for_ubuntu
  <<ENV
  PLEXLOCALAPPDATA="/var/lib/plexmediaserver/Library/Application Support"
  PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR="/var/lib/plexmediaserver/Library/Application Support"
  PYTHONHOME="/usr/lib/plexmediaserver/Resources/Python"
  PLEX_MEDIA_SERVER_HOME="/usr/lib/plexmediaserver"
  PLEX_MEDIA_SERVER_MAX_STACK_SIZE="3000"
  PLEX_MEDIA_SERVER_TMPDIR="/tmp"
  LD_LIBRARY_PATH="/usr/lib/plexmediaserver"
  PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS="6"
  PLEX_FRAMEWORK_PATH="/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/Framework.bundle/Contents/Resources/Versions/2/Python"
ENV
end

def python_unittest(test_file)
  root      = Pathname File.expand_path('../', __FILE__)
  test_file = root.join test_file

  case RUBY_PLATFORM
  when /linux/
    env    = env_for_ubuntu
    python = '/usr/lib/plexmediaserver/Resources/Python/bin/python'
    #python = '/usr/bin/python2.7-dbg -d'
  when /darwin/
    env    = env_for_osx
    python = 'python2.5'
  end

  env = sanitize! env

  `[ -f #{test_file} ] && env #{env} #{python} Contents/Tests/nose_runner.py #{test_file}`
  #`[ -f #{test_file} ] && Contents/Tests/plex-nose-ubuntu #{test_file}`
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

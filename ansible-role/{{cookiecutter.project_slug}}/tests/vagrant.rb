Vagrant.configure(2) do |config|

    # avoid vagrant-vbguest to update the vbox drivers
  config.vbguest.auto_update = false if Vagrant.has_plugin?("vagrant-vbguest")

  config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get -y -qq update
     sudo apt-get install -y -qq python-simplejson python-pip
  SHELL
end

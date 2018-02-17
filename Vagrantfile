# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  config.vm.provision :shell,
    inline: "sh /vagrant/set_up_scripts/vagrant_provisioning_scripts/run.sh"

end

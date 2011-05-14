require 'rubygems'
require 'sinatra'
require 'haml'

module SinatraApp
  class App < Sinatra::Base
    set :sessions, true
    set :public, File.dirname(__FILE__) + '/public'

    get '/' do
      haml :index
    end

    # compute pages
    
    get '/compute_dashboard' do
      haml :compute_dashbaord
    end

    get '/manage_instances' do
      haml :manage_instances
    end

    get '/manage_volumes' do
      haml :manage_volumes
    end

    get '/manage_security' do
      haml :manage_security
    end

    get '/manage_vpn' do
      haml :manage_vpn
    end

    get '/modal' do
      haml :modal, :layout => false
    end

    get '/login_sample' do
      haml :login_sample, :layout => false
    end

    # Object Store Pages
    
    get '/objectstore_dashboard' do
      haml :objectstore_dashboard
    end
    
    get '/manage_rings' do
      haml :manage_rings
    end
    
    get '/manage_devices' do
      haml :manage_devices
    end

    get '/manage_accounts' do
      haml :manage_accounts
    end
    
    

  end
end
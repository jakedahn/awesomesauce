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
    
    get '/compuate_dashboard' do
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




  end
end
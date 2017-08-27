class PagesController < ApplicationController
  before_action :set_submition, only: [:ide]

  def ide

  end

  private

  def set_submition
    # @submition = Submition.new
    @user = User.find(params[:user_id])
    @submition = Submition.get_default(params[:user_id])
  end

end

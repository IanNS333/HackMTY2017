class PagesController < ApplicationController
  before_action :set_submition, only: [:ide]

  def ide

  end

  private

  def set_submition
    # @submition = Submition.new
    @user = User.find(params[:user_id])
    @submition = Submition.get_default(params[:user_id])
    @other_players = User.where('id IN (select user_id from players group by user_id having count(*) > 0)')
                          .where.not(id: @user[:id])
                          .map { |u| [u[:name], u[:id]] }
  end

end

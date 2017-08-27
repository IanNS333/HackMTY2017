class PagesController < ApplicationController
  cattr_accessor :submit_id
  cattr_accessor :just_saved

  @@just_saved = false
  @@submit_id = nil

  def ide
    @user = User.find(params[:user_id])
    @other_players = User.where('id IN (select user_id from players group by user_id having count(*) > 0)')
                          .where.not(id: @user[:id])
                          .map { |u| [u[:name], u[:id]] }
    @other_players = @other_players.map { |u| [u[0], Player.where(user_id: u[1]).order('created_at DESC').limit(1).pluck(:id)[0]] }
    if @@just_saved
      @@just_saved = false
      tmp = Submition.find(@@submit_id)
      @submition = Submition.new do |s|
        s.worldSeed = tmp.worldSeed
        s.playerSeed = tmp.playerSeed
        s.agents = tmp.agents
        s.genotypeLength = tmp.genotypeLength
        s.player1 = tmp.player1
        s.player2 = tmp.player2
        s.user_id = tmp.user_id
      end
      @player1 = Player.find(@submition[:player1])
      @player2 = Player.find(@submition[:player2])
      tmp = 0
      @other_players.each.with_index do |o,i|
        if o[1] == @player2[:id]
          tmp = i
        end
      end
      tmp = @other_players.delete_at(tmp)
      @other_players.insert(0, tmp)
    else
      @submition = Submition.get_default(params[:user_id])
      @player1 = Player.get_default
      @player2 = @other_players[0][1]
    end
    if @player1[:selection] == "tournament"
      @options = [["tournament","tournament"],["random","random"]]
    else
      @options = [["random","random"],["tournament","tournament"]]
    end

  end

  private

end

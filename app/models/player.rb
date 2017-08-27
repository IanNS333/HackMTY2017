class Player < ApplicationRecord

  def self.get_default
    Player.new do |p|
      p.breeding = 1
      p.selection = "tournament"
      p.mutationsPerGenotype = 5
      p.distance = 0.5
      p.pathLength = 0
      p.flatAngle = 0
    end
  end

end

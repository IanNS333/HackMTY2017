class Submition < ApplicationRecord

  def self.get_default(user)
    Submition.new(user_id: user) do |s|
      s.worldSeed = (rand*1000000).to_i
      s.playerSeed = (rand*1000000).to_i
      s.agents = 10
      s.genotypeLength = 150
    end
  end

  def to_python_json
    p1 = Player.find(player1)
    p2 = Player.find(player2)
    "{ \"worldSeed\": #{worldSeed}, \"playerSeed\": #{playerSeed}, \"agents\": #{agents}, \"genotypeLength\": #{genotypeLength}, \"player1\": { \"breeding\": #{p1[:breeding]}, \"selection\": \"#{p1[:selection]}\", \"mutations\": #{p1[:mutationsPerGenotype]}, \"fitness\" : { \"distance\": #{p1[:distance]}, \"pathLength\": #{p1[:pathLength]}, \"flatAngle\": #{p1[:flatAngle]} } }, \"player2\": { \"breeding\": #{p2[:breeding]}, \"selection\": \"#{p2[:selection]}\", \"mutations\": #{p2[:mutationsPerGenotype]}, \"fitness\" : { \"distance\": #{p2[:distance]}, \"pathLength\": #{p2[:pathLength]}, \"flatAngle\": #{p2[:flatAngle]} } } }"
  end

end

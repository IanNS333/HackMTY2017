class CreateSubmitions < ActiveRecord::Migration[5.1]
  def change
    create_table :submitions do |t|
      t.integer :worldSeed
      t.integer :playerSeed
      t.integer :agents
      t.integer :genotypeLength
      t.integer :player1
      t.integer :player2
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end

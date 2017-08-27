class CreatePlayers < ActiveRecord::Migration[5.1]
  def change
    create_table :players do |t|
      t.integer :breeding
      t.text :selection
      t.integer :mutationsPerGenotype
      t.float :distance
      t.float :pathLength
      t.float :flatAngle
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end

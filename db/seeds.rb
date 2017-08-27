# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

User.create(name:"Ky")
User.create(name:"Ger")
User.create(name:"And")
User.create(name:"Ian")
User.create(name:"Test1")
User.create(name:"Test2")

Player.create(breeding: 1, selection: "tournament", mutationsPerGenotype: 19, distance: 0.33, pathLength: -0.33, flatAngle: 0, user_id: 1)
Player.create(breeding: 21, selection: "random", mutationsPerGenotype: 10, distance: 0.5, pathLength: 0.6, flatAngle: -0.5, user_id: 2)
Player.create(breeding: 10, selection: "tournament", mutationsPerGenotype: 8, distance: 0.7, pathLength: 0.3, flatAngle: 0.1, user_id: 3)
Player.create(breeding: 42, selection: "tournament", mutationsPerGenotype: 7, distance: -0.33, pathLength: 0.33, flatAngle: 0.9, user_id: 4)
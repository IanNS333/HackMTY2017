# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/
$(document).on 'click', '#play-button', ->
  x = true

$(document).on 'click', '#stop-button', ->
  x = true

$(document).on 'click', '#submit-button', ->
  $('#submition_worldSeed').val(parseInt(Math.random()*1000000))
  $('#submition_playerSeed').val(parseInt(Math.random()*1000000))
  $('form').trigger('submit.rails')

$(document).on 'click', '#resubmit-button', ->
  $('form').trigger('submit.rails')

$ ->
  $('.slider').slider()
  $('.slider').css({margin: '10px 15px'});
  if $('#sim_res').length>0
    window.j = $('#sim_res').html()
    window.game = new Phaser.Game($("#video").width(), $("#video").height(), Phaser.AUTO, 'video', { preload: preload, create: create, update: update, render: render });
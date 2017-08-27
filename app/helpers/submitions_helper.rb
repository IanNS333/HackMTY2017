module SubmitionsHelper
  def slider value, min, max, step, id, name
    "<span>#{min}</span><input id='#{id}' class='slider' name='#{name}' type='text' class='span2'\
     value='' data-slider-min='#{min}' data-slider-max='#{max}' data-slider-step='#{step}'\
      data-slider-value='#{value}' data-slider-orientation='horizontal' data-slider-selection='after'\
       data-slider-tooltip='show'><span>#{max}</span>".html_safe
  end
end

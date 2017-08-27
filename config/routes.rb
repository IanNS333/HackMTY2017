Rails.application.routes.draw do
  root to: "users#index"

  resources :users, only: [:index] do
    resources :submitions
    resources :players
    get 'ide(/:submit_id)', to: 'pages#ide'
  end

end

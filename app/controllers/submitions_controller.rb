class SubmitionsController < ApplicationController
  before_action :set_submition, only: [:show, :edit, :update, :destroy]

  # GET /submitions
  # GET /submitions.json
  def index
    @submitions = Submition.all
  end

  # GET /submitions/1
  # GET /submitions/1.json
  def show
  end

  # GET /submitions/new
  def new
    @submition = Submition.new
  end

  # GET /submitions/1/edit
  def edit
  end

  # POST /submitions
  # POST /submitions.json
  def create
    @submition = Submition.new(worldSeed: params[:submition][:worldSeed],
                              playerSeed: params[:submition][:playerSeed],
                              agents: params[:submition][:agents],
                              genotypeLength: params[:submition][:genotypeLength],
                              player2: params[:submition][:player2])
    @player1 = Player.new(breeding: params[:submition][:breeding],
                          selection: params[:submition][:selection],
                          mutationsPerGenotype: params[:submition][:mutationsPerGenotype],
                          distance: params[:submition][:distance],
                          pathLength: params[:submition][:pathLength],
                          flatAngle: params[:submition][:flatAngle],
                          user_id: params[:user_id])
    render :new if !@player1.save
    @submition[:player1] = @player1[:user_id]

    puts @submition.to_python_json

    respond_to do |format|
      if @submition.save
        format.html { head :ok }
        format.json { head :ok }
      else
        format.html { render :new }
        format.json { render json: @submition.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /submitions/1
  # PATCH/PUT /submitions/1.json
  def update
    respond_to do |format|
      if @submition.update(submition_params)
        format.html { redirect_to @submition, notice: 'Submition was successfully updated.' }
        format.json { render :show, status: :ok, location: @submition }
      else
        format.html { render :edit }
        format.json { render json: @submition.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /submitions/1
  # DELETE /submitions/1.json
  def destroy
    @submition.destroy
    respond_to do |format|
      format.html { redirect_to submitions_url, notice: 'Submition was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_submition
      @submition = Submition.find(params[:id])
    end
end

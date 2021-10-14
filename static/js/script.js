$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
  });

// Add Recipe Page functionality 
// Add list item to ingredients list when floating button pressed
// Code utilized from stack overflow on suggestion from CI slack channel
// https://stackoverflow.com/questions/53400879/how-to-add-new-item-to-materialize-css-collection

$('#ingredients .add-ingredient-list-item').click(function (event) {
  let IngredientAddItem = `<li class="collection-item">
                              <div class="input-field">
                                  <input name="ingredients" type="text" maxlength="100" pattern="^[A-Za-z0-9 ]*[A-Za-z0-9][A-Za-z0-9 ]*$" required>
                                  <label for="ingredients"> Add Ingredient</label>
                              </div>
                              <a class="remove-list-item">
                                  <i class="fas fa-times"></i>
                                  <span class="sr-only">Remove Ingredient</span>
                              </a>
                          </li>`;
  $(this).parent().before(IngredientAddItem);
});

// Remove ingredient list item on click
$('#ingredients').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});

// Add Method Step item to ingredients list when '+' button hit
$('#recipe-instruction .add-instruction-item').click(function (event) {
  let InstructionAddItem = `<li class="collection-item">
                              <div class="input-field">
                                <textarea name="method_step" class="materialize-textarea" required></textarea>
                               <label for="method_step">Add Description</label>
                              </div>
                              <a class="remove-list-item">
                              <i class="fas fa-times"></i>
                              <span class="sr-only">Remove Description</span>
                          </a>
                          </li>`;
  $(this).parent().before(InstructionAddItem);
});

// Remove Method step item on click
$('#recipe-instruction').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});
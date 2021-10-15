$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();

       // Code from Code Institute Task Manager Project - Validates 'select' inputs from Materialize
       validateMaterializeSelect();

       function validateMaterializeSelect() {
           let classValid = {
               "border-bottom": "1px solid #4caf50",
               "box-shadow": "0 1px 0 0 #4caf50"
           };
           let classInvalid = {
               "border-bottom": "1px solid #f44336",
               "box-shadow": "0 1px 0 0 #f44336"
           };
           if ($("select.validate").prop("required")) {
               $("select.validate").css({
                   "display": "block",
                   "height": "0",
                   "padding": "0",
                   "width": "0",
                   "position": "absolute"
               });
           }
           $(".select-wrapper input.select-dropdown").on("focusin", function () {
               $(this).parent(".select-wrapper").on("change", function () {
                   if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                       $(this).children("input").css(classValid);
                   }
               });
           }).on("click", function () {
               if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                   $(this).parent(".select-wrapper").children("input").css(classValid);
               } else {
                   $(".select-wrapper input.select-dropdown").on("focusout", function () {
                       if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                           if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                               $(this).parent(".select-wrapper").children("input").css(classInvalid);
                           }
                       }
                   });
               }
           });
       }
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

// Add Instruction to list when button pressed
$('#recipe_instruction .add-instruction-list-item').click(function (event) {
  let InstructionAddItem = `<li class="collection-item">
                              <div class="input-field">
                                <textarea name="recipe_instruction" class="materialize-textarea" required></textarea>
                               <label for="recipe_instruction">Add Description</label>
                              </div>
                              <a class="remove-list-item">
                              <i class="fas fa-times"></i>
                              <span class="sr-only">Remove Description</span>
                          </a>
                          </li>`;
  $(this).parent().before(InstructionAddItem);
});

// Remove Method step item on click
$('#recipe_instruction').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});
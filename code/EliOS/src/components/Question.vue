<template>
  <div class="e-form">
    <div class='e-form-question'>
        {{ prompt }}
    </div>
    <div class='e-form-response'>
        <div v-if="type == 'likhert'" class='e-form-likhert-scale'>
            <table>
                <tr>
                    <td><label><input type='radio' name='inp1' v-bind:value="1" v-on="inputListeners" class='e-form-radio'><i class='material-icons'></i></label></td>
                    <td><label><input type='radio' name='inp1' v-bind:value="2" v-on="inputListeners" class='e-form-radio'><i class='material-icons'></i></label></td>
                    <td><label><input type='radio' name='inp1' v-bind:value="3" v-on="inputListeners" class='e-form-radio'><i class='material-icons'></i></label></td>
                    <td><label><input type='radio' name='inp1' v-bind:value="4" v-on="inputListeners" class='e-form-radio'><i class='material-icons'></i></label></td>
                    <td><label><input type='radio' name='inp1' v-bind:value="5" v-on="inputListeners" class='e-form-radio'><i class='material-icons'></i></label></td>
                </tr>
                <tr>
                    <td><i class='material-icons e-form-radio-label'>sentiment_very_dissatisfied</i></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><i class='material-icons e-form-radio-label'>sentiment_very_satisfied</i></td>
                </tr>
            </table>
        </div>
        <div v-else-if="type == 'text'" class='e-form-input-text'>
            <input type="text" class="e-form-text" v-bind:value="value" v-on="inputListeners">
        </div>
        <div v-else-if="type == 'slider'" class='e-form-input-slider'>
            <input type="range" v-bind:min="min" v-bind:max="max" class='e-form-slider' v-bind:value="value" v-on="inputListeners">
            <div class='e-form-slider-value'>{{ value != null ? value : (min + max)/2}}</div>
        </div>
        <div v-else>
            This is not a valid question type
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "question",
  props: {
    prompt: String,
    type: String,
    value: String,
    min: String,
    max: String
  },
  computed: {
    inputListeners: function() {
        var vm = this
        return Object.assign({}, this.$listeners, {
          input: function (event) {
            vm.$emit('input', event.target.value)
          }
        });
    }
  }
};
</script>

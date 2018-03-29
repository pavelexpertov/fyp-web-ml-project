import * as _ from 'lodash'

/*Purpose of the function is to convert fields within an object into
certain types (i.e. converting string that contains a number to an actual number)
Changes happen within the object*/
export default function(dataObj) {
  let newObj = {}
  _.forOwn(dataObj, function(value, key) {
    if (typeof value === "string") {
      if (!isNaN(value)) {
        if (value.indexOf('.') === -1){
          value = Number.parseInt(value)
        }
        else {
          value = Number.parseFloat(value)
        }
        if(Number.isNaN(value))
          value = null
      }
    }
    newObj[key] = value
  })
  return newObj
}

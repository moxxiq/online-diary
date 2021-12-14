export const get_classname = ({class_name, class_number}) => {
    const currentTime = new Date();
    const month = currentTime.getMonth() + 1
    const year = currentTime.getFullYear()

    const number = (year - class_number) + parseInt(month/9)
    
    return `${number}-${class_name}`
}
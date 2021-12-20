export const parse_date = (date_str) => {
    return new Date(Date.parse(date_str)).toISOString().split('T')[0];
};

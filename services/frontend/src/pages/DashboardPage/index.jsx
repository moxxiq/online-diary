import React from "react";
import StudentSubject from "../../components/StudentSubject";
import TeacherJournal from "../../components/TeacherJournal";
import { connect } from "react-redux";

const DashboardPage = ({profile}) => {

  return (
    (profile?.type === 2) ? <TeacherJournal />
    : <StudentSubject/>
  );
};


const mapStateToProps = (rootState) => ({
    profile: rootState?.profile,
  });
  
const mapDispatchToProps = { };
  
export default connect(mapStateToProps, mapDispatchToProps)(DashboardPage);
  
// Generated by gencpp from file proyecto_final/CubosFeedback.msg
// DO NOT EDIT!


#ifndef PROYECTO_FINAL_MESSAGE_CUBOSFEEDBACK_H
#define PROYECTO_FINAL_MESSAGE_CUBOSFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace proyecto_final
{
template <class ContainerAllocator>
struct CubosFeedback_
{
  typedef CubosFeedback_<ContainerAllocator> Type;

  CubosFeedback_()
    : feedback(0)  {
    }
  CubosFeedback_(const ContainerAllocator& _alloc)
    : feedback(0)  {
  (void)_alloc;
    }



   typedef int8_t _feedback_type;
  _feedback_type feedback;





  typedef boost::shared_ptr< ::proyecto_final::CubosFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::proyecto_final::CubosFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct CubosFeedback_

typedef ::proyecto_final::CubosFeedback_<std::allocator<void> > CubosFeedback;

typedef boost::shared_ptr< ::proyecto_final::CubosFeedback > CubosFeedbackPtr;
typedef boost::shared_ptr< ::proyecto_final::CubosFeedback const> CubosFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::proyecto_final::CubosFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::proyecto_final::CubosFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::proyecto_final::CubosFeedback_<ContainerAllocator1> & lhs, const ::proyecto_final::CubosFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.feedback == rhs.feedback;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::proyecto_final::CubosFeedback_<ContainerAllocator1> & lhs, const ::proyecto_final::CubosFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace proyecto_final

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::proyecto_final::CubosFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::proyecto_final::CubosFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::proyecto_final::CubosFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2c99621d1dee505388e972db86733bb8";
  }

  static const char* value(const ::proyecto_final::CubosFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2c99621d1dee5053ULL;
  static const uint64_t static_value2 = 0x88e972db86733bb8ULL;
};

template<class ContainerAllocator>
struct DataType< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "proyecto_final/CubosFeedback";
  }

  static const char* value(const ::proyecto_final::CubosFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback\n"
"int8 feedback\n"
;
  }

  static const char* value(const ::proyecto_final::CubosFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.feedback);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CubosFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::proyecto_final::CubosFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::proyecto_final::CubosFeedback_<ContainerAllocator>& v)
  {
    s << indent << "feedback: ";
    Printer<int8_t>::stream(s, indent + "  ", v.feedback);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROYECTO_FINAL_MESSAGE_CUBOSFEEDBACK_H

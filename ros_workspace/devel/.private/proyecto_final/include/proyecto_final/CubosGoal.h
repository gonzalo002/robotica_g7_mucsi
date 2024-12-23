// Generated by gencpp from file proyecto_final/CubosGoal.msg
// DO NOT EDIT!


#ifndef PROYECTO_FINAL_MESSAGE_CUBOSGOAL_H
#define PROYECTO_FINAL_MESSAGE_CUBOSGOAL_H


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
struct CubosGoal_
{
  typedef CubosGoal_<ContainerAllocator> Type;

  CubosGoal_()
    : order(0)  {
    }
  CubosGoal_(const ContainerAllocator& _alloc)
    : order(0)  {
  (void)_alloc;
    }



   typedef int8_t _order_type;
  _order_type order;





  typedef boost::shared_ptr< ::proyecto_final::CubosGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::proyecto_final::CubosGoal_<ContainerAllocator> const> ConstPtr;

}; // struct CubosGoal_

typedef ::proyecto_final::CubosGoal_<std::allocator<void> > CubosGoal;

typedef boost::shared_ptr< ::proyecto_final::CubosGoal > CubosGoalPtr;
typedef boost::shared_ptr< ::proyecto_final::CubosGoal const> CubosGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::proyecto_final::CubosGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::proyecto_final::CubosGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::proyecto_final::CubosGoal_<ContainerAllocator1> & lhs, const ::proyecto_final::CubosGoal_<ContainerAllocator2> & rhs)
{
  return lhs.order == rhs.order;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::proyecto_final::CubosGoal_<ContainerAllocator1> & lhs, const ::proyecto_final::CubosGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace proyecto_final

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::proyecto_final::CubosGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::proyecto_final::CubosGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::proyecto_final::CubosGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::proyecto_final::CubosGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::proyecto_final::CubosGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::proyecto_final::CubosGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::proyecto_final::CubosGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0bb344a14dad212e50d218aec04eba29";
  }

  static const char* value(const ::proyecto_final::CubosGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0bb344a14dad212eULL;
  static const uint64_t static_value2 = 0x50d218aec04eba29ULL;
};

template<class ContainerAllocator>
struct DataType< ::proyecto_final::CubosGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "proyecto_final/CubosGoal";
  }

  static const char* value(const ::proyecto_final::CubosGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::proyecto_final::CubosGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal definition\n"
"int8 order\n"
;
  }

  static const char* value(const ::proyecto_final::CubosGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::proyecto_final::CubosGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.order);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CubosGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::proyecto_final::CubosGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::proyecto_final::CubosGoal_<ContainerAllocator>& v)
  {
    s << indent << "order: ";
    Printer<int8_t>::stream(s, indent + "  ", v.order);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROYECTO_FINAL_MESSAGE_CUBOSGOAL_H
